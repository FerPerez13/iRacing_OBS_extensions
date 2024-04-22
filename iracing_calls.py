from iracingdataapi.client import irDataClient
import main
import models.login as login
import models.member_profile as m_profile

def try_login():
    print(f"Username: {login.username}, Password: {login.password}")
    idc = irDataClient(username=login.username, password=login.password)

    member_profile = idc.member_profile(cust_id=784776)

    member_info = member_profile.get('member_info')
    name = member_info.get('display_name')

    licenses = member_info.get('licenses')
    m_profile.sportscar_sr = licenses[1].get('safety_rating')
    m_profile.formula_sr = licenses[2].get('safety_rating')
    m_profile.sportscar = licenses[1].get('irating')
    m_profile.formula = licenses[2].get('irating')
