#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length = 0):
    """
    YOUR CODE HERE
    """
    # Your code here
    # example :
#     tickets = [
#     Ticket{ source: "PIT", destination: "ORD" },
#     Ticket{ source: "XNA", destination: "CID" },
#     Ticket{ source: "SFO", destination: "BHM" },
#     Ticket{ source: "FLG", destination: "XNA" },
#     Ticket{ source: "NONE", destination: "LAX" },
#     Ticket{ source: "LAX", destination: "SFO" },
#     Ticket{ source: "CID", destination: "SLC" },
#     Ticket{ source: "ORD", destination: "NONE" },
#     Ticket{ source: "SLC", destination: "PIT" },
#     Ticket{ source: "BHM", destination: "FLG" }
# ]

    # reconstruct it, 
    # put the source as key and destination as value into a dict
    # make a dict
    travel_dict = {}
    for ticket in tickets:
        if ticket.source not in travel_dict:
            travel_dict[ticket.source] = ticket.destination
    route = []
    # make a recursive function
    def get_destination(instance_dict):
        print("instacne dict", instance_dict)
        if instance_dict in travel_dict:
            
            route.append(travel_dict[instance_dict])
            if travel_dict[instance_dict] == "NONE":
                return None
        return get_destination(route[-1])
    
    get_destination("NONE")
    print("Route", route)
    # which would take in a key
    # then it would return the value from the dict
    # then recurse it until the value from the dict is None
    # meanwhile keep track of all the value from that function
    # lets do this







    return route

ticket_1 = Ticket("PIT", "ORD")
ticket_2 = Ticket("XNA", "SAP")
ticket_3 = Ticket("SFO", "BHM")
ticket_4 = Ticket("FLG", "XNA")
ticket_5 = Ticket("NONE", "LAX")
ticket_6 = Ticket("LAX", "SFO")
ticket_7 = Ticket("SAP", "SLC")
ticket_8 = Ticket("ORD", "NONE")
ticket_9 = Ticket("SLC", "PIT")
ticket_10 = Ticket("BHM", "FLG")

tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5,
                   ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]


reconstruct_trip(tickets)