from collections import Counter

def get_domain(email_address):
    """ split on @and return th e last part """ 
    return email_address.lower().split("@")[-1] 

with open("email_addresses.txt") as f:
    domain_counts = Counter(get_domain(line.strip())
                            for line in f
                            if "@" in line
                            )