import json
import openai
from agent import Agent
import time
import os, sys

class suppress_output:
    def __init__(self, suppress_stdout=False, suppress_stderr=False):
        self.suppress_stdout = suppress_stdout
        self.suppress_stderr = suppress_stderr
        self._stdout = None
        self._stderr = None

    def __enter__(self):
        devnull = open(os.devnull, "w")
        if self.suppress_stdout:
            self._stdout = sys.stdout
            sys.stdout = devnull

        if self.suppress_stderr:
            self._stderr = sys.stderr
            sys.stderr = devnull

    def __exit__(self, *args):
        if self.suppress_stdout:
            sys.stdout = self._stdout
        if self.suppress_stderr:
            sys.stderr = self._stderr

openai.api_key = "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"
f = open("compositional_celebrities.json")
data = json.load(f)
category = []
q_and_a=[]
for i in data["data"]:
    if i["category"] in ['birthplace_rounded_lat', 'birthplace_rounded_lng', 'birthplace_tld', 'birthplace_ccn3', 'birthplace_currency', 'birthplace_currency_short', 'birthplace_currency_symbol', 'birthplace_jpn_common_name', 'birthplace_spa_common_name', 'birthplace_rus_common_name', 'birthplace_est_common_name', 'birthplace_urd_common_name', 'birthplace_callingcode', 'birthyear_nobelLiterature', 'birthdate_uspresident', 'birthyear_masterchamp']:
        q_and_a.append((i["Question"],i["Answer"]))
    if i["category"] not in category:
        category.append(i["category"])
agen = Agent(openai.api_key,[], verbose=-1)

counter=0
for j in q_and_a:
    time.sleep(30)
    if counter==2000:
        break
    with suppress_output(suppress_stdout=True, suppress_stderr=True):
        try:
            a=agen.run(j[0],[])
        except:
            a = "agent had an issue"
    print(str(counter)+"|",a[0]+"|",j[1][0])
    counter += 1

