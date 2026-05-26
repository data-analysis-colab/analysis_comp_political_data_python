import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from assets.translations import countries, labels, grammar, titles, captions


@st.cache_data
def load_data(csv_name):
    csv_folder = "app/assets/prepared_csvs/"
    return pd.read_csv(csv_folder + csv_name)


df_cpd = load_data("cpd.csv")
elect_new_predictors = load_data("elect_new_predictors.csv")
elect_cntn_predictors = load_data("elect_cntn_predictors.csv")
elect_comb_predictors = load_data("elect_comb_predictors.csv")

def fmt(val_, decimals=1, lang_="English"):
    if pd.isna(val_):
        return ""
    if lang_ == "Deutsch":
        return f"{val_:.{decimals}f}".replace(".", ",")
    return f"{val_:.{decimals}f}"


fmt_1 = lambda x: fmt(x, 1, lang)
fmt_2 = lambda x: fmt(x, 2, lang)


def plot_predictor(cpd, country_, predictor_):

    country_ = [C["Germany"] if country_ == C["All Countries (Bar Charts only)"] else country_][0]
    plot = cpd[cpd["country"] == country_].copy()

    plot_label_dict = {
        L["Unemployment Rate"]: [
            "unemp", L["Unemployment Rate"], G["Unemployment Rate"],
            L["Unemployment Rate (Pct of Civilian Labour Force)"], "%"
        ],
        L["Inflation Rate"]: [
            "inflation", L["Inflation Rate"], G["Inflation Rate"],
            L["Growth of Consumer Price Index (Pct Change from Prev Year)"], "%"
        ],
        L["Annual Gov. Deficit"]: [
            "deficit", L["Annual Gov. Deficit"], G["Annual Gov. Deficit"],
            L["Annual Government Deficit (Pct of GDP)"], "%"
        ],
        L["GDP Growth"]: [
            "realgdpgr", L["GDP Growth"], G["GDP Growth"],
            L["Growth of Real GDP (Pct Change from Prev Year)"], "%"
        ],
        L["Social Security Transfers"]: [
            "sstran", L["Social Security Transfers"], G["Social Security Transfers"],
            L["Social Security Transfers (Pct of GDP)"], "%"
        ],
        L["Gov. Disbursements"]: [
            "outlays", L["Gov. Disbursements"], G["Gov. Disbursements"],
            L["Total Government Disbursements (Pct of GDP)"], "%"
        ],
        L["Gov. Education Exp."]: [
            "educexp_gov_ipol", L["Gov. Education Exp."], G["Gov. Education Exp."],
            L["Government Education Expenses (Pct of GDP)"], "%"
        ],
        L["Mand. Childcare Exp."]: [
            "childcare_pmp", L["Mand. Childcare Exp."], G["Mand. Childcare Exp."],
            L["Mandatory Childcare Expenses (Pct of GDP)"], "%"
        ],
        L["Disposable Income"]: [
            "postfisc_gini", L["Disposable Income"], G["Disposable Income"],
            L["Pct of Disposable Income after Taxes and Transfers"], "%"
        ]
    }

    gov_party_labels = {
        1.0: L["Right Hegemony"],
        2.0: L["Center-Right Dominance"],
        3.0: L["Balanced Left/Right"],
        4.0: L["Center-Left Dominance"],
        5.0: L["Left Hegemony"]
    }

    y = plot_label_dict[predictor_][0]
    label_short = plot_label_dict[predictor_][1]
    titel_label = plot_label_dict[predictor_][2]
    label_long = plot_label_dict[predictor_][3]
    suffix = plot_label_dict[predictor_][4]

    plot_years_new = plot[plot["elect_new_year"].notnull()]["elect_new_year"].tolist()
    plot_years_cntn = plot[plot["elect_cntn_year"].notnull()]["elect_cntn_year"].tolist()

    plot["gov_party_label"] = plot["gov_party"].map(gov_party_labels)
    plot["prev_gov_party"] = plot["gov_party"].shift(1)
    plot["prev_gov_party_label"] = plot["prev_gov_party"].map(gov_party_labels)

    plot["y_hover"] = plot[y].apply(fmt_1) if y in ["unemp", "postfisc_gini"] else plot[y].apply(fmt_2)

    fig = make_subplots(specs=[[{"secondary_y": False}]])

    # main line
    fig.add_trace(
        go.Scatter(
            x=plot["year"],
            y=plot[y],
            mode="lines",
            line=dict(width=3, color="#76B7B2"),
            xaxis = "x",
            customdata=plot[["y_hover", "gov_party_label"]],
            hovertemplate=(
                "<b>%{x}</b><br>"
                f"{label_short}: " + "%{customdata[0]}" + f"{suffix}<br>"
                f"{L["Cabinet Ideology"]}: "+ "%{customdata[1]}"
                "<extra></extra>"
            )
        )
    )

    # elect new markers
    fig.add_trace(
        go.Scatter(
            x=plot["elect_new_year"],
            y=plot[y],
            mode="markers",
            marker=dict(symbol="diamond", size=12, color="#FFB347", opacity=1),
            xaxis = "x",
            customdata=plot[["y_hover", "prev_gov_party_label", "gov_party_label"]],
            hovertemplate = (
                f"<b>{L["Election"]}: " + "%{x}</b><br>"
                f"{label_short}: " + "%{customdata[0]}" + f"{suffix}<br>"
                f"<b>{L["Cabinet Shift"]}: </b>" + "%{customdata[1]} → %{customdata[2]}"
                "<extra></extra>"
            )
        )
    )

    # elect cntn markers
    fig.add_trace(
        go.Scatter(
            x=plot["elect_cntn_year"],
            y=plot[y],
            mode="markers",
            marker=dict(symbol="circle", size=10, color="#aeb6bf", opacity=1),
            showlegend=False,
            xaxis="x2",
            customdata = plot[["y_hover", "gov_party_label"]],
            hovertemplate = (
                f"<b>{L["Election"]}: " + "%{x}</b><br>"
                f"{label_short}: " + "%{customdata[0]}" + f"{suffix}<br>"
                f"<b>{L["Cabinet Continuity"]}: </b>" + "%{customdata[1]}"
                "<extra></extra>"
            )
        )
    )

    # bottom x-axis (new ideological comp)
    fig.update_xaxes(
        title_text=T["Election Years which Resulted in New Ideological Composition of Cabinet"],
        tickmode="array", tickvals=plot_years_new, showgrid=False, gridwidth=0.5,
    )

    # top x-axis (continuity)
    fig.update_layout(
        xaxis2=dict(
            overlaying="x",
            matches="x",
            side="top",
            tickmode="array",
            tickvals=plot_years_cntn,
            title=T["Election Years which Resulted in Ideological Continuity of Cabinet"],
            showgrid=False,
            gridwidth=0.5
        )
    )

    fig.update_yaxes(title_text=label_long, ticksuffix=suffix)

    for year in plot_years_new:
        fig.add_vline(x=year, line_width=1, line_dash="solid", opacity=0.25)

    for year in plot_years_cntn:
        fig.add_vline(x=year, line_width=1, line_dash="dot", opacity=0.25)

    fig.update_layout(
        title=dict(
            text=f"{T["Temporal Relation between"]} {titel_label} {T["and Election Outcomes"]} ({country_})",
            y=0.97, x=0.5, xanchor="center", yanchor="top", font=dict(size=22)
        ),
        margin=dict(t=120),
        showlegend=False,
        template="plotly_dark",
    )

    return fig


def plot_predictor_comparison(df_, country_, mode_="new"):

    predictor_dict = {
        "unemp": L["Unemployment Rate"],
        "inflation": L["Inflation Rate"],
        "deficit": L["Annual Gov. Deficit"],
        "nld": L["Industrial Disputes"],
        "realgdpgr": L["GDP Growth"],
        "sstran": L["Social Security Transfers"],
        "outlays": L["Gov. Disbursements"],
        "educexp_gov_ipol": L["Gov. Education Exp."],
        "childcare_pmp": L["Mand. Childcare Exp."],
        "postfisc_gini": L["Disposable Income"]
    }

    country_ = C["All Countries"] if country_ == C["All Countries (Bar Charts only)"] else country_
    country_label = f"{len(plot_countries) - 1} {C["Countries"]}" if country_ == C["All Countries"] else country_
    country_data = df_[df_["country"] == country_]

    plot = (
        country_data
            [[cl for cl in country_data.columns if cl.endswith("_perc") and cl[5:-5] in predictor_dict]]
        .unstack()
        .rename(L["Predictive Power"])
        .reset_index()
    )

    plot = plot.rename(columns={"level_0": "Predictor"}).drop(columns="level_1")

    plot[L["Election Count"]] = (
        country_data
            [[cl for cl in country_data.columns if cl.endswith("_count") and cl[5:-6] in predictor_dict]]
        .unstack().values
    )

    for v in plot["Predictor"]:
        if v.startswith("incr_"):
            plot.loc[plot["Predictor"] == v, "Predictor"] = f"{predictor_dict[v[5:-5]]}<br>({L["Increase"]})"
        elif v.startswith("decr_"):
            plot.loc[plot["Predictor"] == v, "Predictor"] = f"{predictor_dict[v[5:-5]]}<br>({L["Decrease"]})"
        else:
            plot.loc[plot["Predictor"] == v, "Predictor"] = predictor_dict[v[5:-5]]

    plot = plot[plot[L["Election Count"]] >= 2] if country_ != C["All Countries"] else plot[plot[L["Predictive Power"]].notna()]
    plot = plot.sort_values(L["Predictive Power"], ascending=False).reset_index(drop=True)

    plot["Direction"] = np.select(
        [plot["Predictor"].str.contains(L["Increase"]), plot["Predictor"].str.contains(L["Decrease"])],
        [L["Increase"], L["Decrease"]], "Combined"
    )

    plot["Predictor"] = pd.Categorical(plot["Predictor"], categories=plot["Predictor"], ordered=True)

    if mode_ == "new":
        title = f"{T["Predictors for the Election of New Governments"]} ({country_label})"
        annot = (f"{CT[
            "Predictive Power = likelihood with which substantial change in economic or government-spending-related indicator is followed by election"
            + "<br>" +
            "resulting in new ideological composition of cabinet. Substantial change = above-average increase/decrease for ≥2 consecutive years."
            + "<br>" +
            "Only election periods separated by ≥2 years included."
        ]}")
    elif mode_ == "cntn":
        title = f"{T["Predictors for the Re-Election of Governments"]} ({country_label})"
        annot = (f"{CT[
            "Predictive Power = likelihood with which substantial change in economic or government-spending-related indicator is followed by election"
            + "<br>" +
            "resulting in continuation of previous ideological composition of cabinet. Substantial change = above-average increase/decrease for ≥2"
            + "<br>" +
            "consecutive years. Only election periods separated by ≥2 years included."
        ]}")
    else:
        title = f"{T["Combined Predictors for Election Outcomes"]} ({country_label})"
        annot = (f"{CT[
            "Combination of the two previous figures; shows the combined average predictive power for each indicator"
            + "<br>" +
            "(increases and decreases) regarding election outcomes (new cabinet or continuation of cabinet)."
        ]}")

    direction_color_map = {
        L["Increase"]: "#5DA5DA",
        L["Decrease"]: "#8c6bb1",
        "Combined": "#76B7B2"
    }

    fig = px.bar(
        plot,
        x=L["Predictive Power"],
        y="Predictor",
        orientation="h",
        color="Direction",
        color_discrete_map=direction_color_map,
        category_orders={"Predictor": plot["Predictor"].tolist()},
        text=L["Predictive Power"],
        custom_data=[plot[L["Election Count"]]]
    )

    fig.update_traces(
        texttemplate="<b>%{text}%</b>",
        textposition="inside",
        insidetextanchor="middle",
        hovertemplate=(
            "<b>%{y}</b><br>"
            "<br>"
            f"{L["Predictive Power"]}: " + "%{x}<br>"
            f"{L["Election Count"]}: " + "%{customdata}<br>"
            "<extra></extra>"
        )
    )

    fig.update_yaxes(title_text="")
    fig.update_xaxes(ticksuffix="%")

    fig.add_vline(x=50, line_dash="dash", opacity=0.5)

    fig.add_annotation(
        text=annot,
        xref="paper",
        yref="paper",
        y=-0.22 if mode_=="comb" else -0.28,
        x=0.475,
        xanchor="center",
        showarrow=False,
    )

    fig.update_layout(
        title=dict(
            text=title,
            y=0.97, x=0.5, xanchor="center", yanchor="top", font=dict(size=22),
        ),
        template="plotly_dark", margin=dict(b=100 if mode_=="comb" else 120), showlegend=False,
    )

    return fig



params = st.query_params

if "lang" not in st.session_state:
    st.session_state.lang = (
        "Deutsch" if params.get("lang") == "de"
        else "English"
    )

with st.container(border=False, gap=None, horizontal_alignment="center"):

    st.segmented_control(
        "", ("English", "Deutsch"), key="lang", label_visibility="collapsed"
    )

    lang = st.session_state.lang
    st.query_params["lang"] = "de" if lang == "Deutsch" else "en"

    C, L, G, T, CT = countries[lang], labels[lang], grammar[lang], titles[lang], captions[lang]

    for df in [df_cpd, elect_new_predictors, elect_cntn_predictors, elect_comb_predictors]:
        df["country"] = df["country"].map(C)

    plot_countries = (
        df_cpd[~df_cpd["country"].isin([C["Canada"], C["Japan"], C["USA"], C["Switzerland"]])]
        .groupby("country")["pop"].max().sort_values(ascending=False).index.tolist()
    )


st.set_page_config(page_title=T["Election Outcome Analysis based on Socioeconomic Indicators"], layout="wide")
st.title(T["Election Outcome Analysis based on Socioeconomic Indicators"], text_alignment="center")
st.space("xxsmall")

col1, col2, col3 = st.columns([1, 4, 1])
col4, col5, col6 = st.columns([1, 2, 1])

with col5:
    with st.container(horizontal_alignment="center", width="stretch"):
        st.markdown(
            "<div style='text-align: center;'>"
            f"{L["Select Country"]}"
            "</div>",
            unsafe_allow_html=True
        )
        country = st.selectbox(
            "", [C["All Countries (Bar Charts only)"]] + plot_countries,
            label_visibility="collapsed", width=300, index=1
        )
        st.space("small")

with col3:
    with st.container(horizontal_alignment="center", width="stretch"):
        st.space("xlarge")
        st.markdown(
            "<div style='text-align: center;'>"
            f"{L["Select Indicator"]}"
            "</div>",
            unsafe_allow_html=True
        )
        predictor = st.selectbox("", [
            L["Unemployment Rate"], L["Gov. Education Exp."], L["Gov. Disbursements"], L["Mand. Childcare Exp."],
            L["Disposable Income"], L["Annual Gov. Deficit"], L["Social Security Transfers"], L["GDP Growth"],
            L["Inflation Rate"]
        ], label_visibility="collapsed", width=250)

with col2:
    fig_line = plot_predictor(df_cpd, country, predictor)
    st.plotly_chart(fig_line, height=550)

col7, col8 = st.columns([2, 2])

with col7:
    fig_comp_new = plot_predictor_comparison(elect_new_predictors, country, mode_="new")
    st.plotly_chart(fig_comp_new, height=550)

with col8:
    fig_comp_cntn = plot_predictor_comparison(elect_cntn_predictors, country, mode_="cntn")
    st.plotly_chart(fig_comp_cntn, height=550)

col9, col10, col11 = st.columns([0.9, 2.2, 0.9])

with col10:
    fig_comp_comb = plot_predictor_comparison(elect_comb_predictors, country, mode_="comb")
    st.plotly_chart(fig_comp_comb, height=550)

st.markdown("---")
st.markdown(
    "<div style='text-align: center;'>"
    "<a href='https://cpds-data.org/'>Dataset</a> • "
    "<a href='https://www.linkedin.com/in/jan-heinrich-sch%C3%BCttler-64b872396/'>LinkedIn</a>"
    "</div>",
    unsafe_allow_html=True
)