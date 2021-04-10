import boto3
import pprint
import subprocess
import json

import globaldata


def select_profile():
    with open('/home/dpatel/.aws/config', 'r') as f:
        lines = f.readlines()
    globaldata.awsProfiles.clear()
    chosen = 0

    profile_n = profile_o = profile_r = ''
    for line in lines:
        if "profile" in line:
            profile_n = (line.strip().replace('[', '').replace(']', '').split(' '))[1]
        if "region" in line:
            profile_r = (line.strip().replace(' ', '')).split('=')[1]
        if "output" in line:
            profile_o = (line.strip().replace(' ', '')).split('=')[1]

        if len(profile_n) > 0 and len(profile_o) > 0 and len(profile_r) > 0:
            if not (profile_n in globaldata.awsProfiles.keys()):
                temp_list = list()
                temp_list.append(profile_r)
                temp_list.append(profile_o)
                globaldata.awsProfiles[profile_n] = temp_list
                profile_n = profile_o = profile_r = ''

    chosen = show_menu(list(globaldata.awsProfiles.keys()))
    return chosen


def show_menu(choices: list):
    if not ("quit" in choices):
        choices.append("quit")

    chosen = choce_id = -1
    max_choice_id = len(choices)

    if_chosen = False
    while not if_chosen:
        print("\n")
        print("\n")
        print("Select numeric id for your option: ")
        choce_id = -1
        for choice in choices:
            choce_id = choce_id + 1
            print(f'Id: {choce_id}: {choice}')
        print("\n")
        try:
            chosen = int(input("Enter your chosen index: "))
            if -1 < chosen < max_choice_id:
                if_chosen = True
        except Exception as e:
            print('You must enter numerical index!')

    return choices[chosen]


if __name__ == "__main__":
    print("Starting clicommander...")
    chosen = 'c'
    while chosen != 'quit':
        chosen = select_profile()
        print(f'You chosen to: {chosen}')