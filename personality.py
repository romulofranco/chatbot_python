"""
The example returns a JSON response whose content is the same as that in
  ../resources/personality-v3-expect2.txt
"""
from __future__ import print_function
import json
from os.path import join, dirname
from watson_developer_cloud import PersonalityInsightsV3

personality_insights = PersonalityInsightsV3(
    version='2016-10-20',
    ## url is optional, and defaults to the URL below. Use the correct URL for your region.
    url='https://gateway.watsonplatform.net/personality-insights/api',
    username='b3d2e6d8-9d5e-4140-875b-a2fc650c4218',
    password='B43cfIgKzisA')

profile = personality_insights.profile('Esse aqui é um teste de Personality insights Esse aqui é um teste de Personality insights Esse aqui é um teste de Personality insights Esse aqui é um teste de Personality insights Esse aqui é um teste de Personality Esse aqui é um teste de Personality insights Esse aqui é um teste de Personality insights Esse aqui é um teste de Personality insights Esse aqui é um teste de Personality insights Esse aqui é um teste de Personality insights Esse aqui é um teste de Personality insights Esse aqui é um teste de Personality insights Esse aqui é um teste de Personality insights Esse aqui é um teste de Personality insights Esse aqui é um teste de Personality insights Esse aqui é um teste de Personality insights', language='es', accept_language='pt-br', content_type='text/plain',raw_scores=True, consumption_preferences=True)
print(json.dumps(profile, indent=2))