from iracingdataapi.client import irDataClient
import main
import models.login as login
import models.member_profile as m_profile

tread_member_profile_update = False

def try_login():
    print(f"Username: {login.username}, Password: {login.password}")
    idc = irDataClient(username=login.username, password=login.password)

    member_profile = idc.member_profile(cust_id=784776)

    member_info = member_profile.get('member_info')
    m_profile.name = member_info.get('display_name')

    licenses = member_info.get('licenses')

    m_profile.sportscar_sr = licenses[1].get('safety_rating')
    m_profile.sportscar = licenses[1].get('irating')

    m_profile.formula_sr = licenses[2].get('safety_rating')
    m_profile.formula = licenses[2].get('irating')


def update_member_profile():
    with open("results/name.txt", 'w') as f:
        f.write(f"{m_profile.name}")
        f.close()

    with open("results/sportscar_sr.txt", 'w') as f:
        f.write(f"{m_profile.sportscar_sr}")
        f.close()

    with open("results/formula_sr.txt", 'w') as f:
        f.write(f"{m_profile.formula_sr}")
        f.close()

    with open("results/sportscar.txt", 'w') as f:
        f.write(f"{m_profile.sportscar}")
        f.close()

    with open("results/formula.txt", 'w') as f:
        f.write(f"{m_profile.formula}")
        f.close()
