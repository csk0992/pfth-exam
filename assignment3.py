# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 15:11:54 2022

@author: fnatm
"""

'''
Note that since the Adventurespejdliga is exclusively handled by danish scout
groups, all printed text within this script is written in danish for ease of use.

I want to be able to get an idea of a given team's eligibility to participate
in a given challenge, so I'll start by creating a class for teams and one for
challenges.

The necessary attributes to determine a team's eligibility are size and age.
Challenges are built with certain group sizes in mind, so teams cannot be too
few or too many.

Similarly, they target specific age intervals, and some even have secondary
age categories to split up the competition. Which group a team falls in is
determined by the oldest participating member of the team.

Lastly, I also want to be able to get a string that tells me all this info
about a given team, which is done by the getTeam() method.
'''

class team:
    def __init__(self, teamName, teamSize, scoutGroup, highestAge, lowestAge):
        self.teamName = teamName
        self.teamSize = teamSize
        self.scoutGroup = scoutGroup
        self.highestAge = highestAge
        self.lowestAge = lowestAge
        
    def getTeam(self):
        return print(f'{self.teamName} består af {self.teamSize} medlemmer. Det ældste medlem er {self.highestAge} år gammel, og det yngste medlem er {self.lowestAge} år gammel. {self.teamName} har base i spejdergruppen {self.scoutGroup}.')

'''
The challenge class needs a range of attributes as well, in order to compare
and check team eligibility. 

Required team size and age range are added to the attributes as lists because 
you don't have to be a specific amount of people or a specific age, 
but can participate if you fall within an interval. 

Also, it's a part of some challenges that the location where everything starts
is kept hidden until just before, so I need to take that into account,
since I still want known locations as an attribute, since those who would find
use in this script would quickly know how far away from a given scout group 
that the challenge takes place. 

Finally, I need a way to similarly get a string that summarizes the most
important information about a given challenge, like with the teams. getChal()
is meant to take the biggest variables into account and accomplish this task.
'''

class challenge:
    def __init__(self, chalName, requiSize=[], ageRange=[], ageRange2=False, chalLocat=None):
        self.chalName = chalName
        self.requiSize = requiSize
        self.ageRange = ageRange
        self.ageRange2 = ageRange2
        self.chalLocat = chalLocat
    
    def getChal(self):
        if self.chalLocat == None and self.ageRange2 == []:
            return print(f'For at deltage i {self.chalName} skal et hold bestå af {self.requiSize[0]} til {self.requiSize[-1]} deltagere. Alle deltagere skal være minimum {self.ageRange[0]} og maximum {self.ageRange[-1]} år gamle. {self.chalName} har ikke afsløret hvor det afholdes.')
        elif self.chalLocat == None and self.ageRange2 != []:
            return print(f'For at deltage i {self.chalName} skal et hold bestå af {self.requiSize[0]} til {self.requiSize[-1]} deltagere. Alle deltagere skal være minimum {self.ageRange[0]} og maximum {self.ageRange[-1]} år gamle for at deltage i den primære konkurrence, men har holdet en eller flere der er {self.ageRange2[0]}+, kan holdet kun deltage i en separat kategori. {self.chalName} har ikke afsløret hvor det afholdes.')
        elif self.chalLocat != None and self.ageRange2 == []:
            return print(f'For at deltage i {self.chalName} skal et hold bestå af {self.requiSize[0]} til {self.requiSize[-1]} deltagere. Alle deltagere skal være minimum {self.ageRange[0]} og maximum {self.ageRange[-1]} år gamle. {self.chalName} starter følgende sted: {self.chalLocat}.')
        else:
            return print(f'For at deltage i {self.chalName} skal et hold bestå af {self.requiSize[0]} til {self.requiSize[-1]} deltagere. Alle deltagere skal være minimum {self.ageRange[0]} og maximum {self.ageRange[-1]} år gamle for at deltage i den primære konkurrence, men har holdet en eller flere der er {self.ageRange2[0]}+, kan holdet kun deltage i en separat kategori. {self.chalName} starter følgende sted: {self.chalLocat}.')

'''
As for the main attraction, I need to be able to compare a given team's attributes
with a given challenge's requirements, and prints out a summarization of the
circumstances.
The checkEligible() function does this by checking for major potential discrepancies
I have determined, such as whether the team's size fits within the requirements
of the challenge, whether the team's ages means they need to be put in a
secondary category, or whether the ages mean they can't participate at all.
'''

def checkEligible(team, challenge):
    if team.teamSize not in challenge.requiSize:
        return print(f'{team.teamName} skal justere deres tilmeldte antal deltagere for at kunne deltage på {challenge.chalName}.')
    elif team.highestAge in challenge.ageRange2:   
        return print(f'{team.teamName} kan kun deltage i {challenge.chalName} i en sekundær kategori.')
    elif team.lowestAge <= challenge.ageRange[0]:
        return print(f'Et eller flere medlemmer af {team.teamName} har ikke den korrekte alder til at deltage i {challenge.chalName}')
    else:
        return print(f'{team.teamName} kan deltage i {challenge.chalName}.')

'''
Two teams I have been a part of in the past, as well as the current set of
challenges that are an official part of the league,
are added as potential examples for the sake of a comprehensive
comparison.

The current set of challenges are going to be relevant for future use of these
classes regardless of use as a script or module, 
so I have added them to the body of code outside of the main() function.

However, the two teams are past examples that are no longer active, and teams
in general change a lot between seasons compared to challenges. With that in
mind, they are only relevant for this script as an example, and are thus part
of main().

To instantiate my two classes and show what they can do, the main() function
checks whether or not Osterejerne are eligible to participate in
Apokalypseløbet, returns the summaries for both the team and challenge to
further explain the attributes of both.
Finally, Fiasko på Flaske's eligibility to participate in Invictusløbet is then
tested to demonstrate a different potential outcome.'''

_24Silkeborg = challenge('24Silkeborg', [3, 4, 5, 6, 7], [10, 11, 12], list(range(13, 99+1)), 'Silkeborg')    
apokalypseløbet = challenge('Apokalypseløbet', [4, 5, 6, 7], [14, 15, 16, 17], list(range(18, 99+1)), 'Fyn')
ccmr = challenge('CCMR', [3, 4, 5, 6, 7, 8], [12, 13, 14, 15, 16], ageRange2=[], chalLocat='Fyn')
dilleløbet = challenge('Dilleløbet', [2], [12, 13, 14, 15, 16], ageRange2=[], chalLocat='Gribskov')
dinizuli = challenge('Dinizuli', [4, 5, 6, 7], [12, 13, 14, 15, 16], ageRange2=[], chalLocat='Nordsjælland')
fenris = challenge('Fenris', [4, 5, 6, 7], [11, 12, 13, 14, 15, 16], ageRange2=[], chalLocat='Trekantsområdet')
invictusløbet = challenge('Invictusløbet', [3, 4, 5, 6], [13, 14, 15, 16, 17], ageRange2=[], chalLocat=None)
nathejk = challenge('Nathejk', [3, 4, 5, 6, 7], [12, 13, 14, 15, 16], list(range(17, 99+1)), 'Sjælland')
solarisløbet = challenge('Solarisløbet', [4, 5, 6, 7], [14, 15, 16, 17], list(range(18, 99+1)), chalLocat=None)
wasa_wasa = challenge('Wasa Wasa', [3, 4, 5, 6, 7, 8], [12, 13, 14, 15, 16], list(range(17, 99+1)), 'Nordjylland')

def main():
    osterejerne = team('Osterejerne', 7, 'Gallerne', 22, 17)
    fiasko_på_flaske = team('Fiasko på Flaske', 5, 'Sortebrødrene', 15, 14)
    
    checkEligible(osterejerne, apokalypseløbet)        
    team.getTeam(osterejerne)
    challenge.getChal(apokalypseløbet)
    checkEligible(fiasko_på_flaske, invictusløbet)
    
if __name__=='__main__':
    main()