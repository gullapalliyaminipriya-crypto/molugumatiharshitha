# Campus Transport Allocation

## 1. Problem Statement

Develop a Python program to manage campus transportation for multiple routes. The program should accept the number of passengers on each route and the seating capacity of each bus. It must calculate the minimum number of buses required for each route, determine the total number of buses needed, identify unserved passengers if bus availability is limited, and display a route-wise transport summary.

## 2. Algorithm

1. Start the program.
2. Read the number of routes.
3. Read the passenger demand for each route.
4. Read the seating capacity of each bus.
5. Read the total number of available buses.
6. Calculate the required buses for each route using ceiling division.
7. Allocate available buses to each route.
8. Calculate the number of passengers served.
9. Identify unserved passengers.
10. Display route-wise details and total buses required.
11. Stop the program.

## 3. Flowchart

\#chatgpt-mermaid-\_r_11e\_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(13, 13, 13);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-\_r_11e\_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_11e\_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_11e\_ .error-icon{fill:rgb(243, 243, 243);}#chatgpt-mermaid-\_r_11e\_ .error-text{fill:rgb(13, 13, 13);stroke:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_11e\_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-\_r_11e\_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-\_r_11e\_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-\_r_11e\_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-\_r_11e\_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-\_r_11e\_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-\_r_11e\_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_11e\_ .marker.cross{stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_11e\_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-\_r_11e\_ p{margin:0;}#chatgpt-mermaid-\_r_11e\_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_11e\_ .cluster-label text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_11e\_ .cluster-label span{color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_11e\_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-\_r_11e\_ .label text,#chatgpt-mermaid-\_r_11e\_ span{fill:rgb(13, 13, 13);color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_11e\_ .node rect,#chatgpt-mermaid-\_r_11e\_ .node circle,#chatgpt-mermaid-\_r_11e\_ .node ellipse,#chatgpt-mermaid-\_r_11e\_ .node polygon,#chatgpt-mermaid-\_r_11e\_ .node path{fill:rgb(222, 234, 251);stroke:rgb(83, 154, 248);stroke-width:1px;}#chatgpt-mermaid-\_r_11e\_ .rough-node .label text,#chatgpt-mermaid-\_r_11e\_ .node .label text,#chatgpt-mermaid-\_r_11e\_ .image-shape .label,#chatgpt-mermaid-\_r_11e\_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-\_r_11e\_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-\_r_11e\_ .rough-node .label,#chatgpt-mermaid-\_r_11e\_ .node .label,#chatgpt-mermaid-\_r_11e\_ .image-shape .label,#chatgpt-mermaid-\_r_11e\_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-\_r_11e\_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-\_r_11e\_ .root .anchor path{fill:rgb(143, 143, 143)!important;stroke-width:0;stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_11e\_ .arrowheadPath{fill:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_11e\_ .edgePath .path{stroke:rgb(143, 143, 143);stroke-width:1px;}#chatgpt-mermaid-\_r_11e\_ .flowchart-link{stroke:rgb(143, 143, 143);fill:none;}#chatgpt-mermaid-\_r_11e\_ .edgeLabel{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-\_r_11e\_ .edgeLabel p{background-color:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_11e\_ .edgeLabel rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_11e\_ .labelBkg{background-color:rgba(252, 252, 252, 0.5);}#chatgpt-mermaid-\_r_11e\_ .cluster rect{fill:rgb(243, 243, 243);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_11e\_ .cluster text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_11e\_ .cluster span{color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_11e\_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(243, 243, 243);border:1px solid rgba(0, 0, 0, 0.1);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-\_r_11e\_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_11e\_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-\_r_11e\_ .icon-shape,#chatgpt-mermaid-\_r_11e\_ .image-shape{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-\_r_11e\_ .icon-shape p,#chatgpt-mermaid-\_r_11e\_ .image-shape p{background-color:rgb(252, 252, 252);padding:2px;}#chatgpt-mermaid-\_r_11e\_ .icon-shape .label rect,#chatgpt-mermaid-\_r_11e\_ .image-shape .label rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_11e\_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-\_r_11e\_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-\_r_11e\_ .node .neo-node{stroke:rgb(83, 154, 248);}#chatgpt-mermaid-\_r_11e\_ [data-look="neo"].node rect,#chatgpt-mermaid-\_r_11e\_ [data-look="neo"].cluster rect,#chatgpt-mermaid-\_r_11e\_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-\_r_11e\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_11e\_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-\_r_11e\_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-\_r_11e\_-gradient);stroke-width:1px;}#chatgpt-mermaid-\_r_11e\_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_11e\_ [data-look="neo"].node .neo-line path{stroke:rgb(83, 154, 248);filter:none;}#chatgpt-mermaid-\_r_11e\_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-\_r_11e\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_11e\_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-\_r_11e\_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-\_r_11e\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_11e\_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-\_r_11e\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_11e\_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(0, 79, 153);}#chatgpt-mermaid-\_r_11e\_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(0, 79, 153);}#chatgpt-mermaid-\_r_11e\_ .node tspan[font-weight="normal"],#chatgpt-mermaid-\_r_11e\_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-\_r_11e\_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-width:1px;}#chatgpt-mermaid-\_r_11e\_ .node rect,#chatgpt-mermaid-\_r_11e\_ .node circle,#chatgpt-mermaid-\_r_11e\_ .node ellipse,#chatgpt-mermaid-\_r_11e\_ .node polygon,#chatgpt-mermaid-\_r_11e\_ .node path{fill:rgb(229, 243, 255);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_11e\_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-\_r_11e\_ .mermaid-decision .label-container{fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-dasharray:2,2;}#chatgpt-mermaid-\_r_11e\_ .edgePaths .flowchart-link{stroke:rgb(143, 143, 143);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-\_r_11e\_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_11e\_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}StartEnter number of routesEnter passenger demand andbus capacityEnter available busesCalculate buses required foreach routeAllocate available busesCalculate served passengersCalculate unserved passengersDisplay transport summaryStop

## 4. Python Source Code

```
# Campus Transport Allocationroutes = int(input("Enter number of routes: "))total_required = 0total_allocated = 0total_unserved = 0demands = []capacities = []for i in range(routes):    print("\nRoute", i + 1)    passengers = int(input("Enter passenger demand: "))    capacity = int(input("Enter bus capacity: "))    if passengers < 0 or capacity <= 0:        print("Invalid input")        exit()    demands.append(passengers)    capacities.append(capacity)available_buses = int(input("\nEnter total available buses: "))if available_buses < 0:    print("Invalid number of buses")    exit()print("\n----- TRANSPORT ALLOCATION -----")remaining_buses = available_busesfor i in range(routes):    passengers = demands[i]    capacity = capacities[i]    required = (passengers + capacity - 1) // capacity    allocated = min(required, remaining_buses)    served = min(passengers, allocated * capacity)    unserved = passengers - served    remaining_buses -= allocated    total_required += required    total_allocated += allocated    total_unserved += unserved    print("\nRoute:", i + 1)    print("Passenger Demand:", passengers)    print("Bus Capacity:", capacity)    print("Buses Required:", required)    print("Buses Allocated:", allocated)    print("Passengers Served:", served)    print("Unserved Passengers:", unserved)print("\n----- FINAL SUMMARY -----")print("Total Buses Required:", total_required)print("Total Buses Allocated:", total_allocated)print("Remaining Buses:", remaining_buses)print("Total Unserved Passengers:", total_unserved)
```

## 5. Sample Input

```
Enter number of routes: 3

Route 1
Enter passenger demand: 100
Enter bus capacity: 50

Route 2
Enter passenger demand: 120
Enter bus capacity: 40

Route 3
Enter passenger demand: 90
Enter bus capacity: 45

Enter total available buses: 6
```

## 6. Sample Output

```
----- TRANSPORT ALLOCATION -----

Route: 1
Passenger Demand: 100
Bus Capacity: 50
Buses Required: 2
Buses Allocated: 2
Passengers Served: 100
Unserved Passengers: 0

Route: 2
Passenger Demand: 120
Bus Capacity: 40
Buses Required: 3
Buses Allocated: 3
Passengers Served: 120
Unserved Passengers: 0

Route: 3
Passenger Demand: 90
Bus Capacity: 45
Buses Required: 2
Buses Allocated: 1
Passengers Served: 45
Unserved Passengers: 45

----- FINAL SUMMARY -----
Total Buses Required: 7
Total Buses Allocated: 6
Remaining Buses: 0
Total Unserved Passengers: 45
```

## 7. Result

The program successfully calculates the buses required for each campus route, allocates the available buses, calculates passengers served, and identifies unserved passengers.
