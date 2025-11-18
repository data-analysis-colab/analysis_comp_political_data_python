class CodeBook:
    def __init__(self, d=None):
        if d is not None:
            for key, value in d.items():
                setattr(self, key, value)


codebook_dict = {
    # General Variables
    "year": "Year of observation",
    "country": "Country names",
    "poco": "Dummy variable with value 1 for post-communist countries",
    "eu": "Dummy variable with value 1 for member states of the European Union (since year of accession)",
    "emu": "Dummy variable with value 1 for member states of the Economic and Monetary Union (EMU) of the European"
           " Union (since year of accession)",

    # Governments
    "gov_right1": "Government composition: cabinet posts of right-wing parties in percentage of total cabinet posts",
    "gov_cent1": "Government composition: cabinet posts of center parties in percentageof total cabinet posts",
    "gov_left1": "Government composition: cabinet posts of social democratic and other left parties in percentage of"
                 " total cabinet posts",
    "gov_party": "Cabinet composition (Schmidt-Index):"
                 "(1) Hegemony of right-wing (and center) parties (gov_left1=0),"
                 "(2) dominance of right-wing (and center) parties (0<gov_left1<=33.33),"
                 "(3) balance of power between left and right (33.33<gov_left1<66.67),"
                 "(4) dominance of social-democratic and other left parties (66.67<=gov_left1<100),"
                 "(5) hegemony of social-democratic and other left parties (gov_left=100).",
    "gov_new": "New ideological composition of cabinet: (0) no change, (1) change: if cabinet ideological composition"
               " (gov_party) changed from last to present year",
    "gov_gap": "‘Ideological gap’ between new and old cabinets. The gap is calculated as the difference of the index"
               " value (gov_party) between the incoming and the outgoing governments",
    "gov_chan": "Number of changes in government per year",
    "gov_right2": "Relative power position of right-wing parties in government based on their seat share in parliament,"
                  " measured in percentage of the total parliamentary seat share of all governing parties",
    "gov_cent2": "Relative power position of center parties in government based on their seat share in parliament,"
                 " measured in percentage of the total parliamentary seat share of all governing parties",
    "gov_left2": "relative power position of social democratic and other left parties in government based on their seat"
                 " share in parliament, measured in percentage of the total parliamentary seat share of all governing"
                 " parties",
    "gov_right3": "parliamentary seat share of right-wing parties in government",
    "gov_cent3": "parliamentary seat share of center parties in government",
    "gov_left3": "parliamentary seat share of social democratic and other left parties in government",
    "gov_sup": "Total government support: seat share of all parties in government",
    "gov_type": "Type of government based on the following classification:"
                "(1) Single-party majority government:"
                "One party takes all governments seats and has a parliamentary majority [>50.0%]."
                "(2) Minimal winning coalition:"
                "All participating parties are necessary to form a majority government [>50.0%]."
                "(3) Surplus coalition:"
                "Coalition governments which exceed the minimal-winning criterion [>50.0%]."
                "(4) Single-party minority government:"
                "The party in government does not possess a majority in Parliament [50.0%]."
                "(5) Multi-party minority government:"
                "The parties in government do not possess a majority in Parliament [50.0%]."
                "(6) Caretaker government:"
                "Governments which should simply maintain the status quo."
                "(7) Technocratic government:"
                "Led by technocratic prime minister, consists of a majority of technocratic ministers"
                "and is in possession of a mandate to change the status quo.",

    # Elections
    "elect": "Date of election of national parliament (lower house). (If there were two elections in a year, the date "
             "of the second is given)",
    "vturn": "Voter turnout in election",
    "womenpar": "Percentage of women in parliaments",

    # Party System
    "rae_ele": "Index of electoral fractionalization of the party system according to the formula proposed by"
               " Rae (1968) [...] The index can take values between 1 (maximal fractionalization) and 0"
               " (minimal fractionalization)",
    "rae_leg": "Index of legislative fractionalization of the party system according to the formula proposed by"
               " Rae (1968) [...] The index can take values between 1 (maximal fractionalization) and 0"
               " (minimal fractionalization)",
    "effpar_ele": "Effective number of parties on the votes level according to the formula [N2] proposed by Laakso"
                  " and Taagepera (1979). The effective number of parties uses the same information as the Rae-Index"
                  " and is calculated from this index as follows: eff par_ele = 1/(1 − rae_ele)",
    "effpar_leg": "Effective number of parties on the seats level according to the formula [N2] proposed by Laakso"
                  " and Taagepera (1979). The effective number of parties uses the same information as the Rae-Index"
                  " and is calculated from this index as follows: eff par_leg = 1/(1 − rae_leg)",

    # Institutions
    "leff": "Effective number of parliamentary parties",
    "lint": "Index of interest group pluralism",
    "structur": "Augmented index of constitutional structures based on Huber et al. (1993, p. 728) [...]. Description:"
                " Additive index composed of five indicators:"
                " (1) federalism (0 = absence, 1= weak, 2 = strong),"
                " (2) parliamentary government = 0, versus presidentialism or other= 1,"
                " (3) proportional representation = 0, modified proportional representation = 1, majoritarian = 2,"
                " (4) bicameralism (0 = no second chamber or second chamber with very weak powers,"
                "    1 = medium strength bicameralism, 2 = strong bicameralism),"
                " (5) frequent referenda = 1.",
    "instcons": "Index of institutional constraints of central state government according to Schmidt (1996); Minimum"
                " value = 0; Maximum value = 6 Range of data: 0 to 5, with high values indicating powerful constraints"
                " and low values indicating that the central government has a great deal of room for manoeuvrability."
                " Description: additive index composed of 6 dummy variables (‘1’ = constraints, ‘0’ = else): (1) EU"
                " membership = 1, (2) degree of centralisation of state structure (federalism = 1), (3) difficulty"
                " of amending constitutions (very difficult = 1) (4) strong bicameralism = 1 (5) central bank"
                " autonomy = 1 (6) frequent referenda =1",
    "fed": "Federalism. Coded: 0 = no; 1 = weak; 2 = strong",
    "pres": "Executive-legislative relations according to Lijphart (2012, pp. 108–110). Coded: 0 = parliamentary"
            " system; 1 = semi-presidential dominated by parliament; 2 = hybrid system; 3 = semi-presidential dominated"
            " by president; 4 = presidential system",
    "prop": "Electoral system: single member districts or proportional representation. Coded 0 = single-member, simple"
            " plurality systems; 1 = modified proportional representation (parallel plurality PR-systems,"
            " majority-plurality/alternative vote); 2 = proportional representation (PR)",
    "bic": "Index of bicameralism according to Lijphart (2012). Coded 1 = unicameralism; 2 = weak bicameralism"
           " (asymmetrical and congruent chambers); 3 = medium strength bicameralism (asymmetrical and incongruent or"
           " symmetrical and congruent); 4 = strong bicameralism (symmetrical and incongruent). (The term “incongruent”"
           " is used when the second chamber is elected by different methods and has the purpose of overrepresenting"
           " certain minorities. The term “symmetrical” refers to equal or moderately unequal constitutional powers and"
           " democratic legitimacy)",
    "referen": "Referendum. Coded 0 = None or infrequent, 1 = frequent",
    "dir": "Index of direct democratic power dispersion (initiatives and referendums). The index contains points for"
           " the degree of majoritarianism or consensualism in the direct democratic provisions in the constitution"
           " and embodied in the decision rules as well as for the actual use of direct democracy. [...]",
    "judrev": "Judicial review (existence of an independent body which decides whether laws are conform to the"
              " constitution). Coded 0 = no, 1 = yes",

    # Openness of the Economy
    "kaopen": "Index for the degree of openness in capital account transactions. [...] The higher the value, the more"
              " open a country is to crossborder capital transactions. The index is normalized to a range between"
              " 0 (minimal openness) and 1 (maximal openness)",
    "openc": "Openness of the economy, measured as total trade (sum of import and export) as a percentage of GDP, in"
             " current prices",

    # Macroeconomic Data
    "outlays": "Total outlays (disbursements) of general government as a percentage of GDP. [...] Disbursements are"
               " transactions of providing financial resources. [...]",
    "receipts": "Total receipts (revenue) of general government as a percentage of GDP",
    "realgdpgr": "Growth of real GDP, percent change from previous year. [...] Real GDP refers to the volume of Gross"
                 " Domestic Product, at constant market prices [...]",
    "nomgdpgr": "Growth of nominal GDP, percent change from previous year. [...] Nominal GDP refers to the value of"
                " Gross Domestic Product, at current market prices [...]",
    "inflation": "Growth of harmonised consumer price index (CPI), all items, percent change from previous year; used"
                 " as a measure for inflation",
    "debt": "Gross general government debt (financial liabilities) as a percentage of GDP",
    "debt_hist": "Gross general government debt (financial liabilities) as a percentage of GDP. The data from the"
                 " variable “debt” is complemented with historical data from the IMF and, in a few cases, from Reinhart"
                 " and Rogoff (2009). Missings in the variable debt are extrapolated using these additional sources.",
    "deficit": "Annual deficit (overall balance / net lending of general government) as a percentage of GDP",
    "pbal": "Annual deficit excluding net interest payments (primary balance of general government) as a percentage of"
            " GDP",
    "capb": "Cyclically adjusted annual deficit excluding net interest payments (cyclically adjusted primary balance of"
            " general government) as a percentage of potential GDP",
    "interest": "Long-term interest rate on government bonds",
    "curac": "Current account balance as a percentage of GDP",

    # Labour Force Data
    "ttl_labf": "Total labour force, in thousands",
    "civ_labf": "Civilian labour force, in thousands",
    "emp_civ": "Civilian employment, in thousands.",
    "labfopar": "Total labour force as a percentage of population",
    "empratio": "Civilian employment as percentage of population",
    "emp_ag": "Civilian employment in agriculture, in thousands",
    "emp_ind": "Civilian employment in industry, in thousands",
    "emp_serv": "Civilian employment in services, in thousands",
    "emp_un": "Unemployed, in thousands",
    "unemp": "Unemployment rate, percentage of civilian labour force",

    # Industrial Disputes and Trade Unions
    "nld": "Number of industrial disputes (strikes and lockouts)",
    "wi": "Workers involved in labour disputes, in thousands",
    "wdlost": "Working days lost (due to strikes and lockouts), in thousands",
    "strike": "Index of strike activity: working days lost per 1000 workers",
    "grossu": "Total reported union members, in thousands",
    "grossu_ipol": "Linear interpolation of variable ‘grossu’",
    "netu": "Net union membership (gross minus independent workers, students, unemployed or retired members),"
            " in thousands",
    "netu_ipol": "Linear interpolation of variable ‘netu’",
    "ud": "Net union membership as a proportion wage and salary earners in employment (union density)",
    "ud_ipol": "Linear interpolation of variable ‘ud’",

     # Public Social Expenditure and Revenue Data
    "sstran": "Social security transfers as a percentage of GDP. Social assistance grants and welfare benefits paid by"
              " general government (benefits for sickness, old-age, family allowances, etc.)",
    "socexp_t_pmp": "Total public and mandatory private social expenditure as a percentage of GDP",
    "oldage_pmp": "Total public and mandatory private expenditure on old age as a percentage of GDP",
    "incapben_pmp": "Total incapacity-related benefits (public and mandatory private) as a percentage of GDP",
    "health_pmp": "Total public and mandatory private expenditure on health as a percentage of GDP",
    "family_pmp": "Total public and mandatory private expenditure for families as a percentage of GDP",
    "almp_pmp": "Total public and mandatory private expenditure on active labour market programmes as a percentage"
                " of GDP.",
    "unemp_pmp": "Cash expenditure for unemployment benefits as a percentage of GDP",
    "housing_pmp": "Total public and mandatory private expenditure on housing as a percentage of GDP",
    "othsocx_pmp": "Public and mandatory private expenditure on other social policy areas as a percentage of GDP",

    # Educational Expenditure and Attainment Data
    "educexp_gov": "General government expenditure on education (current, capital and transfers) as a percentage of"
                   " GDP. It includes expenditure funded by transfers from international sources to government.",
    "educexp_gov_ipol": "Linear interpolation of the variable ‘educexp_gov’",
    "educexp_public": "General government expenditure on education as a percentage of GDP. Includes direct expenditure"
                      " on educational institutions as well as  educational-related public subsidies given to"
                      " households and administered by educational institutions.",
    "educexp_public_ipol": "Linear interpolation of variable ‘educexp_public’",
    "educexp_private": "Expenditure on education from non-educational private sector as a percentage of GDP. Includes"
                       " all direct expenditure on educational institutions and net of public subsidies.",
    "educexp_private_ipol": "Linear interpolation of variable ‘educexp_private’",
    "educatt_minimal": "Share of population attending no more than secondary education",
    "educatt_minimal_ipol": "Linear interpolation of variable ‘educatt_minimal’",
    "educatt_tertiary": "Share of population attending tertiary education",
    "educatt_tertiary_ipol": "Linear interpolation of variable ‘educatt_tertiary’",

    # Labour Market Policy
    "servadmi_pmp": "Public and mandatory private employment services and administration as a percentage of GDP",
    "training_pmp": "Public and mandatory private expenditure on labour market training as a percentage of GDP",
    "jobrot_pmp": "Public and mandatory private expenditure on job rotation and job sharing as a percentage of GDP",
    "incent_pmp": "Public and mandatory private expenditure on employment incentives (recruitment and employment "
                  "maintenance incentives) as a percentage of GDP",
    "disabled_pmp": "Public and mandatory private expenditure on supported employment and (vocational) rehabilitation "
                    "of persons with a reduced working capacity as a percentage of GDP",
    "jobcrea_pmp": "Public and private mandatory expenditure on direct job creation (usually in the public or "
                   "non-profit sector) as a percentage of GDP",
    "startup_pmp": "Public and mandatory private support of unemployed persons (or closely-related groups) starting"
                   " enterprises or becoming self-employed as a percentage of GDP",
    "compen_pmp": "Public and mandatory private unemployment compensation and severance pay (in cash) as a"
                  " percentage of GDP",
    "earretir_pmp": "Public and private mandatory expenditure (in cash) on early retirement for labour market reasons"
                    " as a percentage of GDP",
    "emprot_reg": "Employment protection strictness provided through legislation and as a result of enforcement"
                  " processes (scale of 0-6; higher values indicate stricter employment protection). This indicator"
                  " measures the strictness of regulation of individual dismissal of employees on regular/indefinite"
                  " contracts.",
    "emprot_temp": "Employment protection strictness provided through legislation and as a result of enforcement"
                   " processes (scale of 0-6; higher values indicate stricter employment protection). This indicator"
                   " measures the strictness of regulation on the use of fixed-term and temporary work agency"
                   " contracts.",

    # Family Policy
    "fallow_pmp": "Total public and mandatory private cash benefits for family allowances as a percentage of GDP",
    "mpleave_pmp": "Total public and mandatory private cash benefits for maternal and parental leave as a percentage"
                   " of GDP",
    "childcare_pmp": "Total public and mandatory private social expenditure for childcare and early educational"
                     " services as a percentage of GDP (benefits in kind)",
    "homehelp_pmp": "Total public and mandatory private social expenditure for home-help and accommodation services"
                    " to families with children as a percentage of GDP (benefits in kind)",

    # Income Inequality
    "prefisc_gini": "Gini index of pre-fisc income (before taxes and transfers) among household members aged 18-65,"
                    " in percent. [...] Data available in survey waves every few years."
                    " ['The Gini index measures the extent to which the distribution of income or consumption among"
                    " individuals or households within an economy deviates from a perfectly equal distribution. A Gini"
                    " index of 0 represents perfect equality, while an index of 100 implies perfect inequality.'"
                    " Definition according to the databank.worldbank.org Metadata Glossary]",
    "pretran_gini": "Gini index of pre-transfer income (after taxes, before transfers) among household members aged"
                    " 18-65, in percent. [...] Data available in survey waves every few years."
                    " ['The Gini index measures the extent to which the distribution of income or consumption among"
                    " individuals or households within an economy deviates from a perfectly equal distribution. A Gini"
                    " index of 0 represents perfect equality, while an index of 100 implies perfect inequality.'"
                    " Definition according to the databank.worldbank.org Metadata Glossary]",
    "postfisc_gini": "Gini index of disposable income (after taxes and transfers) among household members aged 18-65,"
                     " in percent. [...] Data available in survey waves every few years."
                     " ['The Gini index measures the extent to which the distribution of income or consumption among"
                    " individuals or households within an economy deviates from a perfectly equal distribution. A Gini"
                    " index of 0 represents perfect equality, while an index of 100 implies perfect inequality.'"
                    " Definition according to the databank.worldbank.org Metadata Glossary]",

    # Demographic Data
    "pop": "Total population, in thousands",
    "pop15_64": "Population 15-64, in thousands.",
    "pop65": "Population over 65, in thousands",
    "elderly": "Population over 65, as a percentage of population",
}


party_family_dict = {"social": "Social Democratic", "leftsoc": "Left-Socialist", "comm": "Communist",
                     "postcom": "Post-Communist", "agrarian": "Agrarian", "conserv": "Conservative",
                     "relig": "Religious", "liberal": "Liberal", "protest": "Protest", "green": "Green",
                     "ethnic": "Ethnic", "right": "Right-Populist", "regio": "Regionalist", "femin": "Feminist",
                     "monarch": "Monarchist", "person": "Personalist", "pension": "Pensioners", "nonlbl": "Non-lable",
                     "allia": "Electoral Alliance", "others": "Others"}


def create_shares_dict(_list):
    import re

    _dict = {}
    for i in _list:
        if i in _list[:(len(_list)//2)]:
            i_type = "votes"
            i_bare = re.sub(r'\d+$', '', i)
        else:
            i_type = "seats"
            i_bare = re.sub(r'\d+$', '', i[1:])
        _dict[i] = (f"Share of {i_type} of the party classified as ‘{i}’. The superordinate party family is classified"
                    f" as ‘{party_family_dict[i_bare]}’")
    return _dict