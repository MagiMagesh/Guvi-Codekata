import re

text_to_search = '''

Avul Pakir Jainulabdeen Abdul Kalam (/ˈæbdəl kəˈlɑːm/ (About this soundlisten); 15 October 1931 – 27 July 2015) 
was an Indian aerospace scientist who served as the 11th President of India from 2002 to 2007. 
He was born and raised in Rameswaram, Tamil Nadu and studied physics and aerospace engineering. 
He spent the next four decades as a scientist and science administrator, mainly at the Defence Research and 
Development Organisation (DRDO) and Indian Space Research Organisation (ISRO) and was intimately involved in India's
 civilian space programme and military missile development efforts.[1] He thus came to be known as the Missile Man of 
 India for his work on the development of ballistic missile and launch vehicle technology.[2][3][4] He also played a 
 pivotal organisational, technical, and political role in India's Pokhran-II nuclear tests in 1998, the first since the original nuclear test by India in 1974.[5]

Kalam was elected as the 11th President of India in 2002 with the support of both the ruling 
Bharatiya Janata Party and the then-opposition Indian National Congress. Widely referred to as the "People's President",[6] 
he returned to his civilian life of education, writing and public service after a single term. He was a recipient of several 
prestigious awards, including the Bharat Ratna, India's highest civilian honour.

While delivering a lecture at the Indian Institute of Management Shillong, Kalam collapsed and died from an apparent 
cardiac arrest on 27 July 2015, aged 83.[7] Thousands, including national-level dignitaries, 
attended the funeral ceremony held in his hometown of Rameswaram, where he was buried with full state honours.[8]

'''

pattern = re.compile(r'\d{4}')

matches = pattern.finditer(text_to_search)

c = []
for match in matches:
    c.append(match)
    print(match.group())
print(len(c))

import random

first_name = ['Ashok','Saraswathi','loganathan','Yosodha','Magesh','Ganesh','Anitha']
last_name = ['Rao','Bai']
a = []
for i in range(100):
    b = random.choice(first_name) + '.'+ random.choice(last_name) + '@gmail.com'
    if b not in a:
        a.append(b)
for i in a:
    pat = re.compile(r'([a-zA-Z0-9-]+\.?[a-zA-Z]+)@([a-z0-9-]+)\.?([a-z]+)')
    mat = pat.finditer(i)
    for i in mat:
        print(i.group(0))