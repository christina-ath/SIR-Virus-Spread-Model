# SIR Virus Spread Model
 
 The project is an atempt to build an SIR virus spread model (Suspected Infected Removed) in order to find the COVID-19 transmition rate given a small set of data from a rural area in Greece

 These differential equations are the base of the SIR model :
    Y' = −αY E
    E' = αY E − βE
    T' = βE

The starting conditions of the problem are Y(0) = 235, E(0) = 14, T(0) = 0

The Data given :


Day    Suspected   Verified 
0         235        14
16        201        22
31        153        29
47        121        21
62        108        8
78        97         8
109       83         0


The way I handled the problem is that first i solve the differential equation using the classic Runge-Kutta numerical method. Then i load the data given and i try to figure out a model that corrects the runge-Kutta produced data so they match the given data as closely as possible using python's optimization libraries and methods. Then i can find the parameters α and β of the aformentioned differential equations.