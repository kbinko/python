class Vault:
    def __init__(self, galeons=0, sickles=0, knuts=0):
        self.galeons = galeons
        self.sickles = sickles
        self.knuts = knuts
    
    def __str__(self):
        return f"{self.galeons} galeons, {self.sickles} sickles, {self.knuts} knuts"

potter = Vault(100, 50, 25)
weasley = Vault(50, 25, 12)

galleons = potter.galeons + weasley.galeons
sickles = potter.sickles + weasley.sickles
knuts = potter.knuts + weasley.knuts

print(f"{galleons} galeons, {sickles} sickles, {knuts} knuts")