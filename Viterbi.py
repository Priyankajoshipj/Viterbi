# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 16:05:30 2018

@author: priya
"""

def viterbi(states,startingProb,obs,Transformation_Mat,Emmision_Mat,Obs_Sequence):
    Obs_Sequence_Char=list(Obs_Sequence)
    obsindex=[]
    #print(Obs_Sequence_Char)
    NofStates=len(states)
    most_likely=[[0 for x in range(NofStates)] for y in range(len(Obs_Sequence))]
    
    #probabilities=[len(Obs_Sequence_Char)]
    alpha=[[0 for x in range(NofStates)] for y in range(len(Obs_Sequence))]
    #print("obs Len",len(Obs_Sequence_Char))
    for m in range(len(Obs_Sequence_Char)):
        obsindex.append(findObsIndex(Obs_Sequence_Char[m],obs))
    #For alpha with starting prob of Hot and cold state
    for i in range(len(Obs_Sequence)):
        for j in range(NofStates):
            alpha[i][j],most_likelyS=calculateAlpha(startingProb,Transformation_Mat,Emmision_Mat,obsindex,i,j,alpha)
            most_likely[i][j]=states[most_likelyS]
    return alpha,most_likely

def calculateAlpha(startingProb,Transformation_Mat,Emmision_Mat,obsindex,i,j,alpha):
    temp_alpha=[]
    
    if(i==0):
        multiplier = startingProb[j]*Emmision_Mat[j][obsindex[i]]
        temp_alpha.append(1)
    else:
        multiplier =Emmision_Mat[j][obsindex[i]]
        a=alpha[i-1]
        
        #print(len(alpha),"len",j,"j",k,"k",Transformation_Mat[k][j])
        for l in range(len(a)):
            #print(a[l],"al",j,"j",Transformation_Mat[j][l],a[l]*Transformation_Mat[j][l])
            temp_alpha.append(a[l]*Transformation_Mat[j][l])
    maxAlpha,likelystate=findMax(temp_alpha)
    aplha = multiplier * maxAlpha
    
    #print("multiplier",multiplier,"max(temp_alpha)",max(temp_alpha))
    return aplha,likelystate
def findMax(a):
    maxA=0
    MaxI=0
    for i in range(len(a)):
        if(a[i]>maxA):
            maxA=a[i]
            MaxI=i
    return maxA,MaxI
def MostLikelyState(most_likely,alpha,states):
    state=[]
    for i in range(len(alpha)):
        maxA,mostlikelystate=findMax(alpha[i])
        ms=most_likely[i][mostlikelystate]
        #state.append(states[mostlikelystate])
        state.append(ms)
    return state
def findObsIndex(Obs_Sequence_Char,obs):
    NofDiffObs=len(obs)
    for i in range(NofDiffObs):
        #print(Obs_Sequence_Char,type(Obs_Sequence_Char),i,type(obs[i]))
        if (Obs_Sequence_Char==str(obs[i])):
           # print(Obs_Sequence_Char,i)
            return i
if __name__ == "__main__":
    
    """NofStates=int(input("Enter number of states for HMM "))
    NofDiffObs=int(input("Enter the possible observations for HMM "))"""
    states=[]
    startingProb=[]
    obs=[]
    states=['Hot','Cold']
    startingProb=[0.8,0.2]
    obs=[1,2,3]
    Emmision_Mat=[[0.2, 0.4, 0.4], [0.5, 0.4, 0.1]]
    Transformation_Mat=[[0.7, 0.4], [0.3, 0.6]]
    probabilities=[]
    most_likely=[]
    MostLikelySeq=[]
    NofStates=2
    NofDiffObs=3
    """for i in range(NofStates):
        s=str(input("Enter State value "))
        p=float(input("Enter starting probability of this State "))
        states.append(s)
        startingProb.append(p)
    for j in range(NofDiffObs):
        o=str(input("Enter Observation "))
        obs.append(o)"""
        
    """Transformation_Mat= [[0 for x in range(NofStates)] for y in range(NofStates)]
    Emmision_Mat=[[0 for x in range(NofDiffObs)] for y in range(NofStates)]


    for i in range(NofStates):
        for j in range(NofDiffObs):
            print("input probability for :",obs[j] ," given ",states[i])
            Emmision_Mat[i][j]=float(input())
    for i in range(NofStates):
        for j in range(NofStates):
            print("input probability for Transformation from:",states[j] ," to state ",states[i])
            Transformation_Mat[i][j]=float(input())"""
    Obs_Sequence=str(input("Enter Observation sequence "))
   
    probability,most_likely=viterbi(states,startingProb,obs,Transformation_Mat,Emmision_Mat,Obs_Sequence)
    #MostLikelyObs=MostLikely()
    Obs_SequenceLen=len(Obs_Sequence)
    lastA=probability[Obs_SequenceLen-1]
    Final_Probability,likeleyState=findMax(lastA)
    MostLikelySeq=MostLikelyState(most_likely,probability,states)
    print("Final Probability is: ",Final_Probability)
    print("Aplha values for state Hot and cold of observations ",Obs_Sequence)
    print(probability)
    
    print("Most likely sequence ",MostLikelySeq)
    print("Most likely states for each alpha ",most_likely)