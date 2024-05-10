from iracingdataapi.client import irDataClient

import models.login as login
import models.member_profile as m_profile

tread_member_profile_update = False


def get_license_html(type, license, irating, sr):
    return f'<head><meta http-equiv="refresh" content="1"></head><html><table><tr><td><img src="../images/iracing_licenses/{type.lower()}_{license.lower()}.svg"></td><td><div style="font-size:125px;color:#fff;font-weight:700;font-family:verdana">{sr}</div><div style="font-size:125px;color:#fff;font-weight:700;font-family:verdana">{irating}</div></td></tr></table></html>'


def try_login():
    idc = irDataClient(username=login.username, password=login.password)
    m_profile.customer_id = idc.member_info().get("cust_id")


def update_member_profile():
    print("Get Licences Info from iRacing...")

    idc = irDataClient(username=login.username, password=login.password)

    member_profile = idc.member_profile(cust_id=m_profile.customer_id)

    member_info = member_profile.get("member_info")
    m_profile.name = member_info.get("display_name")

    licenses = member_info.get("licenses")

    m_profile.oval_license = licenses[0].get("group_name").replace("Class ", "")
    m_profile.oval_sr = licenses[0].get("safety_rating")
    m_profile.oval = licenses[0].get("irating")

    m_profile.sportscar_license = licenses[1].get("group_name").replace("Class ", "")
    m_profile.sportscar_sr = licenses[1].get("safety_rating")
    m_profile.sportscar = licenses[1].get("irating")

    m_profile.formula_license = licenses[2].get("group_name").replace("Class ", "")
    m_profile.formula_sr = licenses[2].get("safety_rating")
    m_profile.formula = licenses[2].get("irating")

    update_member_profile_results()

    print("OVAL License", m_profile.oval_license)
    print("OVAL SR", m_profile.oval_license)
    print("OVAL IR", m_profile.oval_license)
    print()

    print("SPORTSCAR License", m_profile.sportscar_license)
    print("SPORTSCAR SR", m_profile.sportscar_sr)
    print("SPORTSCAR IR", m_profile.sportscar)
    print()

    print("FORMULA License", m_profile.formula_license)
    print("FORMULA SR", m_profile.formula_sr)
    print("FORMULA IR", m_profile.formula)
    print()


def get_last_results():
    idc = irDataClient(username=login.username, password=login.password)
    member_profile = idc.member_profile(cust_id=m_profile.customer_id)

    last_results = member_profile.get("recent_events")
    race_results = [
        result for result in last_results if result.get("event_type") == "RACE"
    ]

    print(race_results[0])


def update_member_profile_results():
    with open("results/sportscar.html", "w") as f:
        f.write(
            get_license_html(
                "sportscar",
                m_profile.sportscar_license,
                m_profile.sportscar,
                m_profile.sportscar_sr,
            )
        )
        f.close()

    with open("results/formula.html", "w") as f:
        f.write(
            get_license_html(
                "formula",
                m_profile.formula_license,
                m_profile.formula,
                m_profile.formula_sr,
            )
        )
        f.close()

    with open("results/oval.html", "w") as f:
        f.write(
            get_license_html(
                "oval", m_profile.oval_license, m_profile.oval, m_profile.oval_sr
            )
        )
        f.close()
