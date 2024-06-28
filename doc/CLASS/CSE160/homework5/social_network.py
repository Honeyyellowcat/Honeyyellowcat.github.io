# Name: Felicity Cundiff
# Date: 5/15/2024
# CSE 160, Spring 2024
# Homework 5

import utils  # noqa: F401, do not remove if using a Mac
import networkx as nx
import matplotlib.pyplot as plt
from operator import itemgetter


###
#  Problem 1a
###

def get_practice_graph():
    """Builds and returns the practice graph
    """
    practice_graph = nx.Graph()
    practice_graph.add_edge("A", "B")
    practice_graph.add_edge("A", "C")
    practice_graph.add_edge("B", "C")

    practice_graph.add_edge("B", "D")
    practice_graph.add_edge("C", "E")
    practice_graph.add_edge("D", "E")

    return practice_graph


def draw_practice_graph(graph):
    """Draw practice_graph to the screen.
    """
    nx.draw_networkx(graph)
    plt.show()


###
#  Problem 1b
###

def get_romeo_and_juliet_graph():
    """Builds and returns the romeo and juliet graph
    """
    rj = nx.Graph()
    rj.add_edge("Romeo", "Juliet")
    rj.add_edge("Romeo", "Friar Laurence")
    rj.add_edge("Juliet", "Friar Laurence")
    rj.add_edge("Juliet", "Nurse")
    rj.add_edge("Romeo", "Benvolio")
    rj.add_edge("Romeo", "Mercutio")
    rj.add_edge("Mercutio", "Benvolio")

    return rj


def draw_rj(graph):
    """Draw the rj graph to the screen and to a file.
    """
    nx.draw_networkx(graph)
    plt.savefig("romeo-and-juliet.pdf")
    plt.show()


###
#  Problem 2
###

def friends(graph, user):
    """Returns a set of the friends of the given user, in the given graph.
    """
    # This function has already been implemented for you.
    # You do not need to add any more code to this (short!) function.
    return set(graph.neighbors(user))


def friends_of_friends(graph, user):
    """Find and return the friends of friends of the given user.

    Arguments:
        graph: the graph object that contains the user and others
        user: unique identifier

    Returns: a set containing the names of all of the friends of
    friends of the user. The set should not contain the user itself
    or their immediate friends.
    """
    user1_friends = friends(graph, user1)
    user2_friends = friends(graph, user2)
    return user1_friends.intersection(user2_friends)
    pass


def num_common_friends_map(graph, user):
    """Returns a map (a dictionary), mapping a person to the number of friends
    that person has in common with the given user. The map keys are the
    people who have at least one friend in common with the given user,
    and are neither the given user nor one of the given user's friends.
    Example: a graph called my_graph and user "X"
    Here is what is relevant about my_graph:
        - "X" and "Y" have two friends in common
        - "X" and "Z" have one friend in common
        - "X" and "W" have one friend in common
        - "X" and "V" have no friends in common
        - "X" is friends with "W" (but not with "Y" or "Z")
    Here is what should be returned:
      num_common_friends_map(my_graph, "X")  =>   { 'Y':2, 'Z':1 }

    Arguments:
        graph: the graph object that contains the user and others
        user: unique identifier

    Returns: a dictionary mapping each person to the number of (non-zero)
    friends they have in common with the user
    """
    user_friends = friends(graph, user)
    common_friends_map = {}
    for friend in graph.nodes():
        if friend != user and friend not in user_friends:
            common_friends_map[friend] = len(common_friends(graph, user, friend))
    return {k: v for k, v in common_friends_map.items() if v > 0}
    pass


def num_map_to_sorted_list(map_with_number_vals):
    """Given a dictionary, return a list of the keys in the dictionary.
    The keys are sorted by the number value they map to, from greatest
    number down to smallest number.
    When two keys map to the same number value, the keys are sorted by their
    natural sort order for whatever type the key is, from least to greatest.

    Arguments:
        map_with_number_vals: a dictionary whose values are numbers

    Returns: a list of keys, sorted by the values in map_with_number_vals
    """
    return sorted(map_with_number_vals, key=lambda x: (-map_with_number_vals[x], x))
    pass


def recs_by_common_friends(graph, user):
    """
    Returns a list of friend recommendations for the user, sorted
    by number of friends in common.

    Arguments:
        graph: the graph object that contains the user and others
        user: a unique identifier

    Returns: A list of friend recommendations for the given user.
    The friend recommendation list consists of names/IDs of people in
    the graph who are not yet a friend of the given user.  The order
    of the list is determined by the number of common friends (people
    with the most common friends are listed first).  In the
    case of a tie in number of common friends, the names/IDs are
    sorted by their natural sort order, from least to greatest.
    """
    user_friends = friends(graph, user)
    recommendations = []
    for friend in graph.nodes():
        if friend != user and friend not in user_friends:
            recommendations.append((friend, len(common_friends(graph, user, friend))))
    recommendations.sort(key=lambda x: (-x[1], x[0]))
    return [rec[0] for rec in recommendations]
    pass


###
#  Problem 3
###

def influence_map(graph, user):
    """Returns a map (a dictionary) mapping from each person to their
    influence score, with respect to the given user. The map only
    contains people who have at least one friend in common with the given
    user and are neither the user nor one of the users's friends.
    See the assignment writeup for the definition of influence scores.
    """
    user_friends = friends(graph, user)
    common_friends_map = {}
    for friend in graph.nodes():
        if friend != user and friend not in user_friends:
            common_friends_map[friend] = len(common_friends(graph, user, friend))
    return common_friends_map
    pass


def recommend_by_influence(graph, user):
    """Return a list of friend recommendations for the given user.
    The friend recommendation list consists of names/IDs of people in
    the graph who are not yet a friend of the given user.  The order
    of the list is determined by the influence score (people
    with the biggest influence score are listed first).  In the
    case of a tie in influence score, the names/IDs are sorted
    by their natural sort order, from least to greatest.
    """
    influence_scores = influence_map(graph, user)
    recommendations = sorted(influence_scores.keys(), key=lambda x: (-influence_scores[x], x))
    return recommendations
    pass


###
#  Problem 5
###

def get_facebook_graph(filename):
    """Builds and returns the facebook graph
    Arguments:
        filename: the name of the datafile
    """
    facebook_graph = nx.Graph()
    with open(filename, 'r') as file:
        for line in file:
            node1, node2 = line.strip().split()  
            facebook_graph.add_edge(node1, node2)
    return facebook_graph
    pass


def test_get_facebook_graph(facebook, filename):
    if (filename == "facebook-links-small.txt"):
        pass
    else:
        assert len(facebook.nodes()) == 63731
        assert len(facebook.edges()) == 817090


def main():
    practice_graph = get_practice_graph()
    # Make sure to comment out this line after you have visually verified 
    # your practice graph. Otherwise, the picture will pop up every time 
    # that you run your program.
    draw_practice_graph(practice_graph)

    rj = get_romeo_and_juliet_graph()
    # Make sure to comment out this line after you have visually verified
    # your rj graph and created your PDF file. Otherwise, the picture will
    # pop up every time that you run your program.
    draw_rj(rj)

    ###
    #  Problem 4
    ###

    print("Problem 4:")
    print()

   
    def num_friends(graph, user):
        """Returns the number of friends the given user has in the given graph."""
        return len(friends(graph, user))

    def max_num_friends(graph):
        """Returns the maximum number of friends any user has in the given graph."""
        return max(num_friends(graph, user) for user in graph.nodes())

    def most_friends(graph):
        """Returns a list of all users with the maximum number of friends in the given graph."""
        max_friends = max_num_friends(graph)
        return [user for user in graph.nodes() if num_friends(graph, user) == max_friends]

    def average_num_friends(graph):
        """Returns the average number of friends per user in the given graph."""
        total_friends = sum(num_friends(graph, user) for user in graph.nodes())
        return total_friends / len(graph.nodes())

    # Test on the practice graph
    practice_graph = get_practice_graph()
    print("Practice Graph Analysis:")
    print(f"Number of friends for user 'A': {num_friends(practice_graph, 'A')}")
    print(f"Maximum number of friends: {max_num_friends(practice_graph)}")
    print(f"Users with the most friends: {most_friends(practice_graph)}")
    print(f"Average number of friends: {average_num_friends(practice_graph):.2f}")
    print()

    # Test on the Romeo and Juliet graph
    rj_graph = get_romeo_and_juliet_graph()
    print("Romeo and Juliet Graph Analysis:")
    print(f"Number of friends for user 'Romeo': {num_friends(rj_graph, 'Romeo')}")
    print(f"Maximum number of friends: {max_num_friends(rj_graph)}")
    print(f"Users with the most friends: {most_friends(rj_graph)}")
    print(f"Average number of friends: {average_num_friends(rj_graph):.2f}")

    ###
    #  Problem 5
    ###

    def get_facebook_graph(filename):
        """Builds and returns the facebook graph
        Arguments:
            filename: the name of the datafile
        """
        facebook_graph = nx.Graph()
        with open(filename, 'r') as file:
            for line in file:
                node1, node2 = line.strip().split()
                facebook_graph.add_edge(node1, node2)
        return facebook_graph

    def test_get_facebook_graph(facebook, filename):
        """Tests the facebook graph for expected number of nodes and edges
        Arguments:
            facebook: the graph object
            filename: the name of the datafile
        """
        if filename == "facebook-links-small.txt":
            expected_nodes = 37
            expected_edges = 91
        else:
            expected_nodes = 63731
            expected_edges = 817090

        assert len(facebook.nodes()) == expected_nodes, f"Expected {expected_nodes} nodes, but got {len(facebook.nodes())}"
        assert len(facebook.edges()) == expected_edges, f"Expected {expected_edges} edges, but got {len(facebook.edges())}"

    def main():
        fb_filename = "facebook-links-small.txt"
        fb_graph = get_facebook_graph(fb_filename)
        test_get_facebook_graph(fb_graph, fb_filename)
        print("Facebook graph loaded and tested successfully.")

    if __name__ == "__main__":
        main()

    ###
    #  Problem 6
    ###
    print()
    print("Problem 6:")
    print()
    def influence_score(graph, user, person):
        """Calculates the influence score of a person with respect to the given user."""
        user_friends = friends(graph, user)
        if person in user_friends:
            return 0  # User's direct friend, influence score is 0
        common_friends_with_user = common_friends(graph, user, person)
        total_influence_score = 0
        for common_friend in common_friends_with_user:
            total_influence_score += len(friends(graph, common_friend))
        return total_influence_score

    ###
    #  Problem 7
    ###
    print()
    print("Problem 7:")
    print()
def recommend_by_influence(graph, user):
    """Return a list of friend recommendations for the given user based on influence scores."""
    influence_scores = {person: influence_score(graph, user, person) for person in graph.nodes() if person != user}
    recommendations = sorted(influence_scores.keys(), key=lambda x: (-influence_scores[x], x))
    return recommendations


    ###
    #  Problem 8
    ###
    print()
    print("Problem 8:")
    print()
def recommend_combined(graph, user, common_friends_weight=0.5):
    """Return a list of friend recommendations for the given user based on a combination of common friends and influence scores."""
    common_friends_recommendations = recs_by_common_friends(graph, user)
    influence_recommendations = recommend_by_influence(graph, user)
    
    # Combine recommendations
    combined_recommendations = []
    for person in set(common_friends_recommendations + influence_recommendations):
        common_friends_score = common_friends_recommendations.index(person) + 1 if person in common_friends_recommendations else float('inf')
        influence_score = influence_recommendations.index(person) + 1 if person in influence_recommendations else float('inf')
        combined_score = common_friends_weight * common_friends_score + (1 - common_friends_weight) * influence_score
        combined_recommendations.append((person, combined_score))
    
    # Sort by combined score
    combined_recommendations.sort(key=lambda x: x[1])
    return [rec[0] for rec in combined_recommendations]

if __name__ == "__main__":
    main()


###
#  Collaboration
###

# ... Write your answer here, as a comment (on lines starting with "#").