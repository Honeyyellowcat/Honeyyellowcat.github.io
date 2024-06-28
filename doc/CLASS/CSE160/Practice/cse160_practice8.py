# Name: Felicity Cundiff
# CSE 160
# Spring 2024
# Checkin 8

from sys import platform as sys_pf
if sys_pf == 'darwin':
    import matplotlib
    matplotlib.use("TkAgg")

import matplotlib.pyplot as plt


# Problem 1
def plot_heart(x, y):
    '''
    Create a plot given the x and y-coordinates, identical to the
    following figure specified in heart_expected.png. Saves the file
    into an image named heart.png.

    Arguments:
        x - list of floats representing x-coordinates to plot
        y - list of floats representing y-coordinates to plot

    Returns: None.
    '''
    # Create the plot
    plt.plot(x, y, color='pink', linewidth=5)
    
    # Set the title and labels
    plt.title("Heart Shape")
    plt.xlabel("x")
    plt.ylabel("y")
    
    # Save the plot to a file
    plt.savefig("heart.png")
    
    # Show the plot
    plt.show()


x = [0.0, 0.01592017311657953, 0.12546207596059317, 0.41293484142614145,
     0.9448637638349007, 1.7631265168342183, 2.8803191572276456,
     4.277774780256799, 5.906420368589671, 7.690403394594481,
     9.53317178545529, 11.32547109731022, 12.954550804786129,
     14.31376286174221, 15.311699849515877, 15.880060309909043,
     15.979541671841423, 15.60323645474055, 14.77722952076229,
     13.558343222639524, 12.029231114703885, 10.291256797849083,
     8.455791391781567, 6.634703488567839, 4.930886711217192,
     3.4296658221485234, 2.19184308035915, 1.2489993194256128,
     0.601462169517735, 0.21911503023905582, 0.044966155751380375,
     0.001150255171237311, -0.003182596239038998, -0.06280475461769673,
     -0.26699447394780546, -0.6906156923887578, -1.3865003992722638,
     -2.3798233380859646, -3.6649805886539286, -5.205259574531561,
     -6.935338271693398, -8.76639816730973, -10.593401457847609,
     -12.303888997544227, -13.787518945503088, -14.945499118187646,
     -15.699074721377995, -15.99631664576088, -15.816606412227193,
     -15.172418676063725, -14.108242656586128, -12.696738480455231,
     -11.03247047783961, -9.223774981190045, -7.383485905077975,
     -5.619342537368211, -4.02493152014183, -2.6719664908450778,
     -1.6045886310825483, -0.8361901787980973, -0.349036991300406,
     -0.09671569275821718, -0.009178186863469806]

y = [5.0, 5.2029872871540315, 5.788182602755194, 6.687118593066485,
     7.794743388649621, 8.981734208445882, 10.10937212636987,
     11.04502727006552, 11.676267039896839, 11.921842761352343,
     11.738292773086032, 11.121547574605383, 10.10363723513183,
     8.745276476064275, 7.125640325217571, 5.330967416893558,
     3.443697203419924, 1.5336595612796935, -0.347572215756921,
     -2.168611221914038, -3.9165313102869104, -5.592123871744795,
     -7.203222344282802, -8.757432220808997, -10.255627992503811,
     -11.68737703601987, -13.029063733996269, -14.244984012008048,
     -15.29114737682919, -16.12105007022445, -16.692347324020762,
     -16.973209090042378, -16.947213533231935, -16.615901620997615,
     -15.998536643680868, -15.129111568712723, -14.051138815880758,
     -12.811156620883931, -11.452124217483389, -10.007912109539003,
     -8.499915339325488, -6.93645427524446, -5.315137990436312,
     -3.6278308820275007, -1.8673739096113144, -0.03485211804061539,
     1.853965328582254, 3.7643234589895957, 5.641340429414093,
     7.4125748405499925, 8.994259820308454, 10.300549632901657,
     11.254586590246317, 11.799821368866397, 11.909873675169512,
     11.595333517246189, 10.906267326894078, 9.929759889617426,
     8.782512164936676, 7.599225812350736, 6.518131508967139,
     5.665464812422489, 5.140890849881237]

# Uncomment the code below to test the function
# ouput plot matches the expected plot
plot_heart(x, y)


# Problem 2
class StreamingService:
    def __init__(self):
        """
        Creates a new streaming service with initially no artists or songs.
        """
        self.song_dict = {}
        
    def add_song(self, artist, song):
        """
        Add a song to the artist's inventory in the streaming service.
        If the artist already exists in the streaming service, add the
        song to the artist's existing catalogue of songs.

        Arguments:
            artist: a string which represents the name of the artist
            song: a string which represents the name of the song

        Returns: None.
        """
        if artist in self.song_dict:
            self.song_dict[artist].add(song)
        else:
            self.song_dict[artist] = {song}

    def song_inventory(self):
        """
        Return a set of tuples with the tuples in the format
        (artist_name, song_name), which represents all of the
        current artists and songs in the streaming service.
        """
        inventory = set()
        for artist, songs in self.song_dict.items():
            for song in songs:
                inventory.add((artist, song))
        return inventory

    def num_artists(self):
        """
        Return the number of unique artists in the streaming service.
        """
        return len(self.song_dict)

# Testing the implementation
s = StreamingService()
empty = StreamingService()

# Test add_song
s.add_song("WayV", "On My Youth")
assert "WayV" in s.song_dict.keys()
assert "On My Youth" in s.song_dict["WayV"]

s.add_song("WayV", "Try My Luck")
assert "WayV" in s.song_dict.keys()
assert "Try My Luck" in s.song_dict["WayV"]

s.add_song("Olivia Rodrigo", "vampire")
assert "Olivia Rodrigo" in s.song_dict.keys()
assert "vampire" in s.song_dict["Olivia Rodrigo"]

# Test song_inventory
assert s.song_inventory() == {("WayV", "On My Youth"),
                              ("WayV", "Try My Luck"),
                              ("Olivia Rodrigo", "vampire")}
assert empty.song_inventory() == set()

# Test num_artists
assert s.num_artists() == 2
assert empty.num_artists() == 0

