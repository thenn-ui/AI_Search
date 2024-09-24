# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    e = Directions.EAST
    n = Directions.NORTH
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()
    
    visitedlist = []
    stack = util.Stack()
    currentstate = problem.getStartState()
    #print currentstate
    stack.push(((currentstate, '0', 0), None))

    #do dfs from the start state. just reach the goal state
    count = 0
    while not problem.isGoalState(currentstate):
        #print currentstate
        count += 1
        visitedlist.append(currentstate)
        possiblesuccessors = problem.getSuccessors(currentstate)
        #print "possible successors for state: ", currentstate, "= ", possiblesuccessors
        successorlist = [successor for successor in possiblesuccessors if successor[0] not in visitedlist]
        #print(successorlist)
        
        # no successor
        if successorlist == []:
            stack.pop()
        for successor in successorlist:
            stack.push((successor, currentstate))
        
        currentframe = stack.pop()
        currentstate = currentframe[0][0]
        stack.push(currentframe)
        #print count
    #print count
    #found the goal:

    action_sequence = []
    parentstate = None
    while not stack.isEmpty():
        frame = stack.pop()
        state = frame[0][0]
        action = frame[0][1]

        if parentstate == None or parentstate == state and action != '0':
            action_sequence.append(frame[0][1])
            #print frame, parentstate
            parentstate = frame[1]
        #else:
         #   print "something wrong", parentstate, state
    #print action_sequence
    #print(len(action_sequence))
    return list(reversed(action_sequence))


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    visitedlist = []
    bfsqueue = util.Queue()
    stack = util.Stack()

    currentstate = problem.getStartState()
    #print currentstate
    #bfsqueue.push(((currentstate, '0', 0), None)) ###?????? gets pushed twice?

    #do dfs from the start state. just reach the goal state

    while not problem.isGoalState(currentstate):
        visitedlist.append(currentstate)
        possiblesuccessors = problem.getSuccessors(currentstate)
        #print "possible successors for state: ", currentstate, "= ", possiblesuccessors
        successorlist = [successor for successor in possiblesuccessors if successor[0] not in visitedlist]
        #print "current state = ", currentstate, "successor list = ", successorlist
        
        for successor in successorlist:
            #print successor
            bfsqueue.push((successor, currentstate))
            print "current state = ", currentstate, "successor list = ", successorlist
        
        currentframe = bfsqueue.pop()
        currentstate = currentframe[0][0]

        while currentstate in visitedlist:
           currentframe = bfsqueue.pop()
           currentstate = currentframe[0][0]
            

        stack.push(currentframe)
        #print count
    #print count
    #found the goal:

    action_sequence = []
    
    frame = stack.pop()
    state = frame[0][0]
    action = frame[0][1]
    action_sequence.append(action)
    parentstate = frame[1]
    print "########################"
    while not stack.isEmpty():
        frame = stack.pop()
        state = frame[0][0]
        action = frame[0][1]
        #print "action = ", action, "frame = ",frame
        #print "state = ", state
        #print "parent state = ", parentstate
        if parentstate == state and action != '0':
            action_sequence.append(action)
            print "frame = ", frame, 
            print "parentstate = ", parentstate
            parentstate = frame[1]
        #else:
         #   print "something wrong", parentstate, state
    #print action_sequence
    #print(len(action_sequence))
    return list(reversed(action_sequence))

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()
    visitedlist = []
    pqueue = util.PriorityQueue()
    stack = util.Stack()
    
    currentstate = problem.getStartState()
    currentframe = ((currentstate, "0", 0), None, 0, [])
    mincostgoalstateframe = None
    pqueue.push(currentframe, 0)

    while not pqueue.isEmpty():

        currentframe = pqueue.pop()
        currentstate = currentframe[0][0]
        #print "current frame = ", currentframe

        if currentstate in visitedlist: #no answer derived
            #print currentstate, "Already present in visited list"
            continue

        if problem.isGoalState(currentstate):
            if mincostgoalstateframe == None:
                mincostgoalstateframe = currentframe
            elif mincostgoalstateframe[0][2] > currentstate[2]:
                mincostgoalstateframe = currentframe

        visitedlist.append(currentstate)
        #print("visitedlist = ", visitedlist)
        possiblesuccessors = problem.getSuccessors(currentstate)
        #print "possible successors for state: ", currentstate, "= ", possiblesuccessors
        successorlist = [successor for successor in possiblesuccessors if successor[0] not in visitedlist]
        #print(successorlist)
        
        for successor in successorlist:   
            reqdactions = []
            reqdactions.extend(currentframe[3]) #add all actions taken till now
            reqdactions.append(successor[1])
            ########### [state   | parent state |    total cost to get here | actionlist]
            totalcost = currentframe[2] + successor[2]
            pqueue.push((successor, currentstate, totalcost, reqdactions), totalcost)
            #print "From state: ", currentstate, "to: ", successor, "total cost", totalcost

    #print mincostgoalstateframe
    return mincostgoalstateframe[3]

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()
    #visitedlist = set() WORKS for question 4!!
    visitedlist = []
    pqueue = util.PriorityQueue()
    
    startstate = problem.getStartState()
    ################  stateframe   | parent state | g(n) | action sequence
    fcost = 0 + heuristic(startstate, problem)
    currentframe = ((startstate, "0", 0), None, 0, [])
    mincostgoalstateframe = None
    pqueue.push(currentframe, fcost)

    while not pqueue.isEmpty():

        currentframe = pqueue.pop()
        currentstate = currentframe[0][0]

        if currentstate in visitedlist:
            continue
        
        print "current frame = ", currentframe
        print "current state = ", currentstate
        print "mincostgoal frame = ", mincostgoalstateframe
        if mincostgoalstateframe != None: 
            print "mincostgoalframe[2]" , mincostgoalstateframe[2]
        print "currentframe[2]", currentframe[2]
        if problem.isGoalState(currentstate):
            if mincostgoalstateframe == None:
                mincostgoalstateframe = currentframe
            elif mincostgoalstateframe[2] > currentframe[2]: # based on only g since h = 0 at goal state
                mincostgoalstateframe = currentframe
                # do you want to expand the goal state's successors?

        #visitedlist.add(currentstate) WORKS FOR Q 4
        visitedlist.append(currentstate)
        #print "visited list = ", visitedlist
        possiblesuccessors = problem.getSuccessors(currentstate)
        #print "possible successors for state: ", currentstate, "= ", possiblesuccessors
        successorlist = [successor for successor in possiblesuccessors if successor[0] not in visitedlist]
        print "from:", currentstate, "successor list = ", successorlist
        
        for successor in successorlist:   
            reqdactions = []
            reqdactions.extend(currentframe[3]) #add all actions taken till now
            reqdactions.append(successor[1])
            ########### [state   | parent state |    total cost = total cost to get here | actionlist]
            gcost = currentframe[2] + successor[2] # true cost to reach the successor
            hcost = heuristic(successor[0], problem) #from the successor to the goal, what is the heuristic
            fcost = gcost + hcost # estimated cost to reach the goal (eval function)
            pqueue.push((successor, currentstate, gcost, reqdactions), fcost)
            print "From state: ", currentstate, "to: ", successor, "total true cost = ", gcost, "heuristic cost = ", hcost, "fcost = ", fcost

    #print mincostgoalstateframe
    return mincostgoalstateframe[3]


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
