# ideas

just had some brainwaves, wanna write it down

## seperate processes

have view and controller entirely seperate, as in have them be seperate processes and hand info back and fourth between them

> what will this achieve?

textual is pretty slow, meaning that it wont block the rest of the program, we can just queue messages if tx is busy

> how much complexity will this create?

now that view and cont/stat/engi are different processes, an interface will need to be created between the two

## only send actions

ive decided that actually the distrubutor is going to act kinda like a normal server, with the single added bonus that you can run the engine on your own

> what will this achieve?

clients using modified copies of the game will have a much more difficult time, and it will save networking costs for most clients

> how much complexity will this create?

it will actually reduce complexity, because now clients dont need to communicate (but the diagram is kinda inacurate now)
