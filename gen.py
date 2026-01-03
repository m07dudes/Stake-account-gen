import tls_client
import json
import random
import string
from twocaptcha import TwoCaptcha
import re
import time
import base64
import threading
from colorama import Fore

red = Fore.LIGHTRED_EX
blue = Fore.LIGHTBLUE_EX
green = Fore.LIGHTGREEN_EX


session = tls_client.Session(client_identifier="firefox_120")

user = "60d4c3a038d0a53245eb2__cr.mx"
password = "8873857283523"
ip = "premiumresidential.sigmaproxies.com"
port = "823"

proxies = {
                'http': f'http://{user}:{password}@{ip}:{port}',
                'https': f'http://{user}:{password}@{ip}:{port}'
            }


solver = TwoCaptcha(apiKey="2CAPCTHA_KEY_HERE")  # noqa: E501 | Add your 2Captcha Key!


class Gen(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        try:
            def create_pass(x):
                return ''.join(random.choice(
                    string.digits
                    + string.ascii_letters) for _ in range(x))

            password = create_pass(15)

            headers = {
                "accept": "application/ld+json",
                "Origin": "https://mail.tm",
                "Referer": "https://mail.tm/",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"  # noqa: E501
            }

            domain = session.get("https://api.mail.tm/domains",
                                 proxy=proxies,
                                 headers=headers,
                                 ).json()["hydra:member"][0]["domain"]  # noqa: E501

            user = create_pass(10)

            email_account = session.post("https://api.mail.tm/accounts",
                                         proxy=proxies,
                                         headers=headers,
                                         json={"address": f"{user}@{domain}",
                                               "password": password}).json()
            email = email_account["address"]
            id = email_account["id"]
            print(f"{email}:{password}:{id}")

            token = solver.turnstile(sitekey="0x4AAAAAAAGD4gMGOTFnvupz",
                                     url="https://stake.com")["code"]

            headers = {
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.8',
                'access-control-allow-origin': '*',
                'content-type': 'application/json',
                'origin': 'https://stake.com',
                'priority': 'u=1, i',
                'referer': 'https://stake.com/?c=CHANGE_TO_YOUR_AFF_CODE&tab=register&modal=auth',  # Noqa: E501
                'sec-ch-ua': '"Brave";v="143", "Chromium";v="143", "Not A(Brand";v="24"',  # Noqa: E501
                'sec-ch-ua-arch': '"x86"',
                'sec-ch-ua-bitness': '"64"',
                'sec-ch-ua-full-version-list': '"Brave";v="143.0.0.0", "Chromium";v="143.0.0.0", "Not A(Brand";v="24.0.0.0"',  # Noqa: E501
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-model': '""',
                'sec-ch-ua-platform': '"Windows"',
                'sec-ch-ua-platform-version': '"19.0.0"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'sec-gpc': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',  # Noqa: E501
                'x-language': 'en',
                'x-operation-name': 'RegisterUser',
                'x-operation-type': 'query',
            }

            json_data = {
                'query': 'mutation RegisterUser($name: String!, $password: String!, $email: String!, $turnstileToken: String!, $sessionName: String!, $code: String, $signupCode: String, $blackbox: String, $dob: Date!, $countryCode: String, $phoneNumber: String, $clickId: String) {\n  registerUser(\n    name: $name\n    password: $password\n    email: $email\n    turnstileToken: $turnstileToken\n    code: $code\n    signupCode: $signupCode\n    sessionName: $sessionName\n    blackbox: $blackbox\n    dob: $dob\n    countryCode: $countryCode\n    phoneNumber: $phoneNumber\n    clickId: $clickId\n  ) {\n    ...UserAuthenticatedSession\n  }\n}\n\nfragment UserAuthenticatedSession on UserAuthenticatedSession {\n  token\n  session {\n    ...UserSession\n    user {\n      ...UserAuth\n    }\n  }\n}\n\nfragment UserSession on UserSession {\n  id\n  sessionName\n  ip\n  country\n  city\n  active\n  updatedAt\n}\n\nfragment UserAuth on User {\n  id\n  name\n  email\n  dob\n  phoneNumber\n  hasPhoneNumberVerified\n  hasEmailVerified\n  hasPassword\n  intercomHash\n  intercomJwt\n  createdAt\n  hasTfaEnabled\n  hasOauth\n  isMaxBetEnabled\n  isReferred\n  isSportsbookExcluded\n  registeredWithVpn\n  kycBasic {\n    id\n    country\n    birthday\n  }\n  flags {\n    flag\n    createdAt\n  }\n  signupCode {\n    code {\n      code\n    }\n  }\n  roles {\n    name\n  }\n  optionalFeatures\n  balances {\n    ...UserBalance\n  }\n  activeClientSeed {\n    id\n    seed\n  }\n  previousServerSeed {\n    id\n    seed\n  }\n  activeDepositBonus {\n    status\n    minDepositValue\n    maxDepositValue\n    maxBetMultiplier\n    bonusMultiplier\n    expectedAmountMultiplier\n    currency\n    currencyType\n  }\n  activeServerSeed {\n    id\n    seedHash\n    nextSeedHash\n    nonce\n    blocked\n  }\n  veriffStatus\n  verifications {\n    userVerification {\n      ...UserVerification\n    }\n    ageVerification {\n      ...AgeVerification\n    }\n    addressVerification {\n      ...AddressVerification\n    }\n    documentVerification {\n      ...DocumentVerification\n    }\n    riskVerification {\n      ...RiskVerification\n    }\n    employmentVerification {\n      ...EmploymentVerification\n    }\n  }\n  termsOfService {\n    status\n  }\n  veriffBiometricVerificationStatus\n  notificationCount\n}\n\nfragment UserBalance on UserBalance {\n  available {\n    amount\n    currency\n  }\n  vault {\n    amount\n    currency\n  }\n}\n\nfragment UserVerification on IdentityUserVerification {\n  status\n  verified\n}\n\nfragment AgeVerification on IdentityAgeVerification {\n  id\n  active\n  birthDate\n  createdAt\n  expireAt\n  type\n  user {\n    id\n    name\n  }\n  verified\n}\n\nfragment AddressVerification on IdentityAddressVerification {\n  active\n  city\n  country\n  createdAt\n  expireAt\n  id\n  state\n  street\n  type\n  user {\n    id\n    name\n  }\n  verified\n  zip\n}\n\nfragment DocumentVerification on IdentityDocumentVerification {\n  active\n  createdAt\n  documentBirthDate\n  documentCity\n  documentCountry\n  documentExpiry\n  documentFirstName\n  documentId\n  documentLastName\n  documentNationality\n  documentState\n  documentStreet\n  documentType\n  documentZip\n  expireAt\n  id\n  type\n  user {\n    id\n    name\n  }\n  verified\n}\n\nfragment RiskVerification on IdentityRiskVerification {\n  active\n  createdAt\n  expireAt\n  id\n  nationalityCountry\n  nonPoliticallyExposed\n  nonThirdPartyAccount\n  preferredName\n  type\n  user {\n    id\n    name\n  }\n  verified\n}\n\nfragment EmploymentVerification on IdentityEmploymentVerification {\n  active\n  createdAt\n  employerCity\n  employerCountry\n  employerName\n  employerPhone\n  employerState\n  employerStreet\n  employerZip\n  expireAt\n  id\n  type\n  user {\n    id\n    name\n  }\n  verified\n  occupation\n}',  # Noqa: E501
                'variables': {
                    'browser': 'Chrome',
                    'browserVersion': '143',
                    'device': 'Windows PC',
                    'os': 'Windows',
                    'email': str(email),
                    'name': str(user),
                    'password': str(password),
                    'dob': '2000-02-05',
                    'code': 'CHANGE_TO_YOUR_AFF_CODE',
                    'turnstileToken': str(token),
                    'sessionName': 'Chrome (Windows PC)',
                    'blackbox': '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',  # Noqa: E501
                },
            }

            x = session.post(
                'https://stake.com/_api/graphql',
                proxy=proxies,
                headers=headers,
                json=json_data).json()
            print(x)

            if "errors" in x:
                print("Error")
                print(x)
                pass

            stake_token = x["data"]["registerUser"]["token"]

            print(f"Stake: {email}:{password}:{stake_token}")

            headers = {
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'access-control-allow-origin': '*',
                'content-type': 'application/json',
                'origin': 'https://stake.com',
                'priority': 'u=1, i',
                'referer': 'https://stake.com/?tab=register&modal=auth',
                'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',  # noqa: E501
                'sec-ch-ua-arch': '"x86"',
                'sec-ch-ua-bitness': '"64"',
                'sec-ch-ua-full-version': '"141.0.7390.76"',
                'sec-ch-ua-full-version-list': '"Google Chrome";v="141.0.7390.76", "Not?A_Brand";v="8.0.0.0", "Chromium";v="141.0.7390.76"',  # noqa: E501
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-model': '""',
                'sec-ch-ua-platform': '"Windows"',
                'sec-ch-ua-platform-version': '"19.0.0"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',  # noqa: E501
                'x-access-token': stake_token,
                'x-language': 'en',
                'x-operation-name': 'AcceptTermsOfService',
                'x-operation-type': 'query',
            }

            json_data = {
                'query': 'mutation AcceptTermsOfService($termsId: String!) {\n  acceptTermsOfService(termsId: $termsId) {\n    acceptedAt\n  }\n}',  # noqa: E501
                'variables': {
                    'termsId': '713899ac-3365-4e69-92f9-cd3865756ae1',
                },
            }

            response = session.post('https://stake.com/_api/graphql',
                                    proxy=proxies,
                                    headers=headers,
                                    json=json_data).status_code

            time.sleep(10)

            headers = {
                'accept': 'application/json',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/json',
                'origin': 'https://mail.tm',
                'priority': 'u=1, i',
                'referer': 'https://mail.tm/',
                'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',  # noqa: E501
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',  # noqa: E501
            }

            json_data = {
                'address': email,
                'password': password,
            }

            token = session.post('https://api.mail.tm/token',
                                 proxy=proxies,
                                 headers=headers,
                                 json=json_data).json()["token"]

            headers = {
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.5',
                'authorization': f'Bearer {token}',
                'if-none-match': '"9dcb30d704b3123917f0019b3ba68fd5"',
                'origin': 'https://mail.tm',
                'priority': 'u=1, i',
                'referer': 'https://mail.tm/',
                'sec-ch-ua': '"Brave";v="143", "Chromium";v="143", "Not A(Brand";v="24"',  # Noqa: E501
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'sec-gpc': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',  # Noqa: E501
            }

            response = session.get('https://api.mail.tm/messages',
                                   proxy=proxies,
                                   headers=headers).json()["hydra:member"]
            for i in response:
                if "verify" in i["intro"].lower():
                    id = i["id"]

            headers = {
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'authorization': f'Bearer {token}',
                'if-none-match': '"4cae6cf34d20d7a83efef28d2aa85cb8"',
                'origin': 'https://mail.tm',
                'priority': 'u=1, i',
                'referer': 'https://mail.tm/',
                'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',  # noqa: E501
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',  # noqa: E501
            }

            response = session.get(f'https://api.mail.tm/messages/{id}',
                                   proxy=proxies,
                                   headers=headers).json()["text"]

            regex = r"\b\d{6}\b"

            match = re.search(regex, response)
            six_code = match.group()
            print(f"{red}Code: {six_code}{Fore.RESET}")

            headers = {
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'access-control-allow-origin': '*',
                'content-type': 'application/json',
                'origin': 'https://stake.com',
                'priority': 'u=1, i',
                'referer': 'https://stake.com/settings?modal=walletSetup',
                'sec-ch-ua': '"Brave";v="143", "Chromium";v="143", "Not A(Brand";v="24"',  # Noqa: E501
                'sec-ch-ua-arch': '"x86"',
                'sec-ch-ua-bitness': '"64"',
                'sec-ch-ua-full-version-list': '"Brave";v="143.0.0.0", "Chromium";v="143.0.0.0", "Not A(Brand";v="24.0.0.0"',  # Noqa: E501
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-model': '""',
                'sec-ch-ua-platform': '"Windows"',
                'sec-ch-ua-platform-version': '"19.0.0"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'sec-gpc': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',  # Noqa: E501
                'x-access-token': stake_token,  # Noqa: E501
                'x-language': 'en',
                'x-operation-name': 'ConfirmUserEmailCode',
                'x-operation-type': 'query',
            }

            json_data = {
                'query': 'mutation ConfirmUserEmailCode($code: String!) {\n  confirmUserEmailCode(code: $code) {\n    ...UserAuth\n  }\n}\n\nfragment UserAuth on User {\n  id\n  name\n  email\n  dob\n  phoneNumber\n  hasPhoneNumberVerified\n  hasEmailVerified\n  hasPassword\n  intercomHash\n  intercomJwt\n  createdAt\n  hasTfaEnabled\n  hasOauth\n  isMaxBetEnabled\n  isReferred\n  isSportsbookExcluded\n  registeredWithVpn\n  kycBasic {\n    id\n    country\n    birthday\n  }\n  flags {\n    flag\n    createdAt\n  }\n  signupCode {\n    code {\n      code\n    }\n  }\n  roles {\n    name\n  }\n  optionalFeatures\n  balances {\n    ...UserBalance\n  }\n  activeClientSeed {\n    id\n    seed\n  }\n  previousServerSeed {\n    id\n    seed\n  }\n  activeDepositBonus {\n    status\n    minDepositValue\n    maxDepositValue\n    maxBetMultiplier\n    bonusMultiplier\n    expectedAmountMultiplier\n    currency\n    currencyType\n  }\n  activeServerSeed {\n    id\n    seedHash\n    nextSeedHash\n    nonce\n    blocked\n  }\n  veriffStatus\n  verifications {\n    userVerification {\n      ...UserVerification\n    }\n    ageVerification {\n      ...AgeVerification\n    }\n    addressVerification {\n      ...AddressVerification\n    }\n    documentVerification {\n      ...DocumentVerification\n    }\n    riskVerification {\n      ...RiskVerification\n    }\n    employmentVerification {\n      ...EmploymentVerification\n    }\n  }\n  termsOfService {\n    status\n  }\n  veriffBiometricVerificationStatus\n  notificationCount\n}\n\nfragment UserBalance on UserBalance {\n  available {\n    amount\n    currency\n  }\n  vault {\n    amount\n    currency\n  }\n}\n\nfragment UserVerification on IdentityUserVerification {\n  status\n  verified\n}\n\nfragment AgeVerification on IdentityAgeVerification {\n  id\n  active\n  birthDate\n  createdAt\n  expireAt\n  type\n  user {\n    id\n    name\n  }\n  verified\n}\n\nfragment AddressVerification on IdentityAddressVerification {\n  active\n  city\n  country\n  createdAt\n  expireAt\n  id\n  state\n  street\n  type\n  user {\n    id\n    name\n  }\n  verified\n  zip\n}\n\nfragment DocumentVerification on IdentityDocumentVerification {\n  active\n  createdAt\n  documentBirthDate\n  documentCity\n  documentCountry\n  documentExpiry\n  documentFirstName\n  documentId\n  documentLastName\n  documentNationality\n  documentState\n  documentStreet\n  documentType\n  documentZip\n  expireAt\n  id\n  type\n  user {\n    id\n    name\n  }\n  verified\n}\n\nfragment RiskVerification on IdentityRiskVerification {\n  active\n  createdAt\n  expireAt\n  id\n  nationalityCountry\n  nonPoliticallyExposed\n  nonThirdPartyAccount\n  preferredName\n  type\n  user {\n    id\n    name\n  }\n  verified\n}\n\nfragment EmploymentVerification on IdentityEmploymentVerification {\n  active\n  createdAt\n  employerCity\n  employerCountry\n  employerName\n  employerPhone\n  employerState\n  employerStreet\n  employerZip\n  expireAt\n  id\n  type\n  user {\n    id\n    name\n  }\n  verified\n  occupation\n}',  # Noqa: E501
                'variables': {
                    'code': str(six_code),
                },
            }

            response = session.post(
                'https://stake.com/_api/graphql',
                proxy=proxies,
                headers=headers,
                json=json_data).json()
            print(response)

            with open("data.json", encoding="utf-8") as f:
                xxx = json.load(f)
                f.close()

            data = random.choice(xxx)
            image = data["id_address"]

            with open(f"C:/Users/m07/Desktop/Projects/StakeGen/example/{image}",  # Noqa: E501 | Just put PATH OF DOCS
                      'rb') as img_file:
                sex = img_file.read()
                encoded_string = base64.b64encode(sex).decode("utf-8")

            headers = {
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'access-control-allow-origin': '*',
                'content-type': 'application/json',
                'origin': 'https://stake.com',
                'priority': 'u=1, i',
                'referer': 'https://stake.com/?tab=register&modal=walletSetup',
                'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',  # noqa: E501
                'sec-ch-ua-arch': '"x86"',
                'sec-ch-ua-bitness': '"64"',
                'sec-ch-ua-full-version': '"141.0.7390.76"',
                'sec-ch-ua-full-version-list': '"Google Chrome";v="141.0.7390.76", "Not?A_Brand";v="8.0.0.0", "Chromium";v="141.0.7390.76"',  # noqa: E501
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-model': '""',
                'sec-ch-ua-platform': '"Windows"',
                'sec-ch-ua-platform-version': '"19.0.0"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',  # noqa: E501
                'x-access-token': stake_token,
                'x-language': 'en',
                'x-operation-name': 'UpdateBasicKyc',
                'x-operation-type': 'query',
            }

            json_data = {
                'query': 'mutation UpdateBasicKyc($firstName: String!, $lastName: String!, $birthday: Date!, $phoneNumber: String, $address: String!, $zipCode: String!, $city: String!, $country: CountryEnum!, $placeOfBirth: CountryEnum!, $industry: String!, $occupation: String!, $occupationExperience: String!) {\n  updateBasicKyc(\n    firstName: $firstName\n    lastName: $lastName\n    birthday: $birthday\n    phoneNumber: $phoneNumber\n    address: $address\n    zipCode: $zipCode\n    city: $city\n    country: $country\n    industry: $industry\n    occupation: $occupation\n    occupationExperience: $occupationExperience\n    placeOfBirth: $placeOfBirth\n  ) {\n    id\n    country\n  }\n}',  # noqa: E501
                'variables': {
                    'lastName': data["last_name"],
                    'firstName': data["first_name"],
                    'zipCode': data["zip_code"],
                    'country': data["min_country"],
                    'placeOfBirth': data["min_country"],
                    'address': data["country"],
                    'city': data["city"],
                    'birthday': data["born_date"],
                    'industry': 'Other-freelancer',
                    'occupation': '',
                    'occupationExperience': '',
                },
            }

            response = session.post('https://stake.com/_api/graphql',
                                    proxy=proxies,
                                    headers=headers,
                                    json=json_data).json()
            print(response)

            IDGEN = create_pass(10)

            headers = {
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/json',
                'origin': 'https://stake.com',
                'priority': 'u=1, i',
                'referer': 'https://stake.com/settings/verification',
                'sec-ch-ua': '"Brave";v="143", "Chromium";v="143", "Not A(Brand";v="24"',  # Noqa: E501
                'sec-ch-ua-arch': '"x86"',
                'sec-ch-ua-bitness': '"64"',
                'sec-ch-ua-full-version-list': '"Brave";v="143.0.0.0", "Chromium";v="143.0.0.0", "Not A(Brand";v="24.0.0.0"',  # Noqa: E501
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-model': '""',
                'sec-ch-ua-platform': '"Windows"',
                'sec-ch-ua-platform-version': '"19.0.0"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'sec-gpc': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',  # Noqa: E501
                'x-access-token': str(stake_token),
            }

            json_data = [
                {
                    'name': f'identity_{IDGEN}',
                    'mimeType': 'image/png',
                    'body': str(encoded_string),
                },
            ]

            sex9532 = session.post('https://stake.com/_api/cdn/file',
                                   proxy=proxies,
                                   headers=headers,
                                   json=json_data).json()
            idDOC = sex9532[0]["id"]
            print(f"{Fore.LIGHTRED_EX}{sex9532}{Fore.RESET}")

            headers = {
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'access-control-allow-origin': '*',
                'content-type': 'application/json',
                'origin': 'https://stake.com',
                'priority': 'u=1, i',
                'referer': 'https://stake.com/settings/verification',
                'sec-ch-ua': '"Brave";v="143", "Chromium";v="143", "Not A(Brand";v="24"',  # Noqa: E501
                'sec-ch-ua-arch': '"x86"',
                'sec-ch-ua-bitness': '"64"',
                'sec-ch-ua-full-version-list': '"Brave";v="143.0.0.0", "Chromium";v="143.0.0.0", "Not A(Brand";v="24.0.0.0"',  # Noqa: E501
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-model': '""',
                'sec-ch-ua-platform': '"Windows"',
                'sec-ch-ua-platform-version': '"19.0.0"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'sec-gpc': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',  # Noqa: E501
                'x-access-token': str(stake_token),
                'x-language': 'en',
                'x-operation-name': 'UpdateExtendedKyc',
                'x-operation-type': 'query',
            }

            json_data = {
                'query': 'mutation UpdateExtendedKyc($identityDocument: String!, $secondaryDocument: String) {\n  updateExtendedKyc(\n    identityDocument: $identityDocument\n    secondaryDocument: $secondaryDocument\n  ) {\n    id\n  }\n}',  # Noqa: E501
                'variables': {
                    'identityDocument': str(idDOC),
                },
            }

            response = session.post('https://stake.com/_api/graphql',
                                    proxy=proxies,
                                    headers=headers,
                                    json=json_data).json()
            print(response)

            headers = {
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'access-control-allow-origin': '*',
                'content-type': 'application/json',
                'origin': 'https://stake.com',
                'priority': 'u=1, i',
                'referer': 'https://stake.com/?tab=register&modal=walletSetup',
                'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',  # noqa: E501
                'sec-ch-ua-arch': '"x86"',
                'sec-ch-ua-bitness': '"64"',
                'sec-ch-ua-full-version': '"141.0.7390.76"',
                'sec-ch-ua-full-version-list': '"Google Chrome";v="141.0.7390.76", "Not?A_Brand";v="8.0.0.0", "Chromium";v="141.0.7390.76"',  # noqa: E501
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-model': '""',
                'sec-ch-ua-platform': '"Windows"',
                'sec-ch-ua-platform-version': '"19.0.0"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',  # noqa: E501
                'x-access-token': stake_token,
                'x-language': 'en',
                'x-operation-name': 'UserKycInfo',
                'x-operation-type': 'query',
            }

            json_data = {
                'query': 'query UserKycInfo($stakeKycEnabled: Boolean = false, $veriffEnabled: Boolean = false, $singleKycEnabled: Boolean = false) {\n  isDiscontinuedBlocked\n  user {\n    id\n    roles {\n      name\n    }\n    optionalFeatures\n    kycStatus\n    dob\n    createdAt\n    hasEmailVerified\n    phoneNumber\n    phoneCountryCode\n    hasPhoneNumberVerified\n    email\n    registeredWithVpn\n    isBanned\n    isSuspended\n    isFiatWithdrawOnly\n    isFiatSuspended\n    resubmitVerification {\n      level\n    }\n    isSuspendedSportsbook\n    alternateNames: cashierAlternateNames {\n      firstName\n      lastName\n      currency\n    }\n    nationalId {\n      nationalId\n      expireDate\n      issueDate\n    }\n    ...StakeKyc @include(if: $stakeKycEnabled)\n    ...Veriff @include(if: $veriffEnabled)\n    ...StakeFiatCountryConfiguration @include(if: $stakeKycEnabled)\n    ...StakeFiatCountryConfiguration @include(if: $singleKycEnabled)\n    ...KycDenmark @include(if: $singleKycEnabled)\n  }\n}\n\nfragment StakeKyc on User {\n  isKycBasicRequired\n  isKycExtendedRequired\n  isKycFullRequired\n  isKycUltimateRequired\n  kycBasic {\n    ...UserKycBasic\n  }\n  kycExtended {\n    ...UserKycExtended\n  }\n  kycFull {\n    ...UserKycFull\n  }\n  kycUltimate {\n    ...UserKycUltimate\n  }\n  transactionEligibilityState {\n    ...UserTransactionEligibilityStateFragment\n  }\n  isKycBypassed\n}\n\nfragment UserKycBasic on UserKycBasic {\n  active\n  address\n  birthday\n  city\n  country\n  createdAt\n  firstName\n  id\n  lastName\n  phoneNumber\n  rejectedReason\n  status\n  updatedAt\n  zipCode\n  placeOfBirth\n  industry\n  occupation\n  occupationExperience\n}\n\nfragment UserKycExtended on UserKycExtended {\n  id\n  active\n  createdAt\n  id\n  rejectedReason\n  status\n}\n\nfragment UserKycFull on UserKycFull {\n  active\n  createdAt\n  id\n  rejectedReason\n  status\n}\n\nfragment UserKycUltimate on UserKycUltimate {\n  id\n  active\n  createdAt\n  id\n  rejectedReason\n  status\n}\n\nfragment UserTransactionEligibilityStateFragment on UserTransactionEligibilityState {\n  fiat {\n    ...FiatTransactionEligibilityStateFragment\n  }\n  crypto {\n    ...CryptoTransactionEligibilityStateFragment\n  }\n  useLegacyLogic\n  requirementVersion\n}\n\nfragment FiatTransactionEligibilityStateFragment on FiatTransactionEligibilityState {\n  currency\n  depositEnabled\n  withdrawalEnabled\n}\n\nfragment CryptoTransactionEligibilityStateFragment on CryptoTransactionEligibilityState {\n  depositEnabled\n  withdrawalEnabled\n}\n\nfragment Veriff on User {\n  veriffStatus\n  veriffUser {\n    reason\n  }\n}\n\nfragment StakeFiatCountryConfiguration on User {\n  fiatCountryConfiguration {\n    country\n    flag\n    nationalIdRequired\n    alternateName {\n      userVisibleInstructions\n      regex\n      firstNamePresentedFirst\n    }\n    currencies {\n      name\n      withdrawal {\n        visible\n        enabled\n      }\n      deposit {\n        visible\n        enabled\n      }\n    }\n  }\n}\n\nfragment KycDenmark on User {\n  kycDenmark {\n    firstName\n    lastName\n    birthDate\n    isValid\n  }\n  mitIdValidationStatus {\n    validStatus\n    reason\n  }\n}',  # noqa: E501
                'variables': {
                    'stakeKycEnabled': True,
                    'veriffEnabled': False,
                    'singleKycEnabled': False,
                },
            }

            response = session.post('https://stake.com/_api/graphql',
                                    proxy=proxies,
                                    headers=headers,
                                    json=json_data).json()
            print(response)

            zenci = [entry for entry in xxx if entry != data]
            with open("data.json", "w", encoding="utf-8") as f:  # Noqa: E501 | data.json for documents PASSPORT ETC
                json.dump(zenci, f, ensure_ascii=False, indent=4)

            x = f"{user}@{domain}:{password}:{stake_token}"

            with open("acc.txt", "a") as f:
                f.write(x+"\n")
                f.close()
        except Exception as er:  # Noqa: E722
            print(er)

def ASCI():
    print(f"""{Fore.RED}

                 ░██████   ░██████████   ░███    ░██     ░██ ░██████████
                ░██   ░██      ░██      ░██░██   ░██    ░██  ░██
                ░██            ░██     ░██  ░██  ░██   ░██   ░██
                ░████████      ░██    ░█████████ ░███████    ░█████████
                       ░██     ░██    ░██    ░██ ░██   ░██   ░██
                ░██   ░██      ░██    ░██    ░██ ░██    ░██  ░██
                 ░██████       ░██    ░██    ░██ ░██     ░██ ░██████████
{Fore.RESET}\n\n                                {Fore.LIGHTRED_EX}Made by m07dudes{Fore.RESET}""")  # Noqa: E501


if __name__ == "__main__":
    while True:
        ASCI()
        gen_account = input(str("                         Enter Number for gen accounts: "))  # Noqa: E501
        for _ in range(int(gen_account)):
            x = Gen().run()
        else:
            0
