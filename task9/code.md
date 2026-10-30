# Smart Electricity Billing for Multiple Apartments

## 1. Problem Statement

Develop a Python program to calculate electricity bills for multiple apartments in an apartment complex. The program should calculate electricity charges based on units consumed using progressive tariff rates, add fixed charges, apply eligible rebates, identify billing discrepancies, and rank apartments according to their electricity consumption.

## 2. Algorithm

1. Start the program.
2. Read the number of apartments.
3. For each apartment, read:
   - Apartment number
   - Previous meter reading
   - Current meter reading
   - Recorded bill amount
4. Calculate electricity consumption:

`Units = Current Reading - Previous Reading`

5. Calculate electricity charges using progressive tariff rates:
   - First 100 units: ₹2 per unit
   - Next 100 units: ₹3 per unit
   - Above 200 units: ₹5 per unit
6. Add fixed charges of ₹50.
7. Apply a 10% rebate if consumption is below 100 units.
8. Calculate the final bill.
9. Compare the calculated bill with the recorded bill.
10. Identify billing discrepancies.
11. Rank apartments according to electricity consumption.
12. Display apartment-wise billing details and ranking.
13. Stop.

## 3. Flowchart

\#chatgpt-mermaid-\_r_sf\_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(13, 13, 13);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-\_r_sf\_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_sf\_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_sf\_ .error-icon{fill:rgb(243, 243, 243);}#chatgpt-mermaid-\_r_sf\_ .error-text{fill:rgb(13, 13, 13);stroke:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_sf\_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-\_r_sf\_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-\_r_sf\_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-\_r_sf\_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-\_r_sf\_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-\_r_sf\_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-\_r_sf\_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_sf\_ .marker.cross{stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_sf\_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-\_r_sf\_ p{margin:0;}#chatgpt-mermaid-\_r_sf\_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_sf\_ .cluster-label text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_sf\_ .cluster-label span{color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_sf\_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-\_r_sf\_ .label text,#chatgpt-mermaid-\_r_sf\_ span{fill:rgb(13, 13, 13);color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_sf\_ .node rect,#chatgpt-mermaid-\_r_sf\_ .node circle,#chatgpt-mermaid-\_r_sf\_ .node ellipse,#chatgpt-mermaid-\_r_sf\_ .node polygon,#chatgpt-mermaid-\_r_sf\_ .node path{fill:rgb(222, 234, 251);stroke:rgb(83, 154, 248);stroke-width:1px;}#chatgpt-mermaid-\_r_sf\_ .rough-node .label text,#chatgpt-mermaid-\_r_sf\_ .node .label text,#chatgpt-mermaid-\_r_sf\_ .image-shape .label,#chatgpt-mermaid-\_r_sf\_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-\_r_sf\_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-\_r_sf\_ .rough-node .label,#chatgpt-mermaid-\_r_sf\_ .node .label,#chatgpt-mermaid-\_r_sf\_ .image-shape .label,#chatgpt-mermaid-\_r_sf\_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-\_r_sf\_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-\_r_sf\_ .root .anchor path{fill:rgb(143, 143, 143)!important;stroke-width:0;stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_sf\_ .arrowheadPath{fill:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_sf\_ .edgePath .path{stroke:rgb(143, 143, 143);stroke-width:1px;}#chatgpt-mermaid-\_r_sf\_ .flowchart-link{stroke:rgb(143, 143, 143);fill:none;}#chatgpt-mermaid-\_r_sf\_ .edgeLabel{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-\_r_sf\_ .edgeLabel p{background-color:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_sf\_ .edgeLabel rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_sf\_ .labelBkg{background-color:rgba(252, 252, 252, 0.5);}#chatgpt-mermaid-\_r_sf\_ .cluster rect{fill:rgb(243, 243, 243);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_sf\_ .cluster text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_sf\_ .cluster span{color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_sf\_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(243, 243, 243);border:1px solid rgba(0, 0, 0, 0.1);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-\_r_sf\_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_sf\_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-\_r_sf\_ .icon-shape,#chatgpt-mermaid-\_r_sf\_ .image-shape{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-\_r_sf\_ .icon-shape p,#chatgpt-mermaid-\_r_sf\_ .image-shape p{background-color:rgb(252, 252, 252);padding:2px;}#chatgpt-mermaid-\_r_sf\_ .icon-shape .label rect,#chatgpt-mermaid-\_r_sf\_ .image-shape .label rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_sf\_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-\_r_sf\_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-\_r_sf\_ .node .neo-node{stroke:rgb(83, 154, 248);}#chatgpt-mermaid-\_r_sf\_ [data-look="neo"].node rect,#chatgpt-mermaid-\_r_sf\_ [data-look="neo"].cluster rect,#chatgpt-mermaid-\_r_sf\_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-\_r_sf\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_sf\_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-\_r_sf\_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-\_r_sf\_-gradient);stroke-width:1px;}#chatgpt-mermaid-\_r_sf\_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_sf\_ [data-look="neo"].node .neo-line path{stroke:rgb(83, 154, 248);filter:none;}#chatgpt-mermaid-\_r_sf\_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-\_r_sf\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_sf\_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-\_r_sf\_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-\_r_sf\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_sf\_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-\_r_sf\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_sf\_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(0, 79, 153);}#chatgpt-mermaid-\_r_sf\_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(0, 79, 153);}#chatgpt-mermaid-\_r_sf\_ .node tspan[font-weight="normal"],#chatgpt-mermaid-\_r_sf\_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-\_r_sf\_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-width:1px;}#chatgpt-mermaid-\_r_sf\_ .node rect,#chatgpt-mermaid-\_r_sf\_ .node circle,#chatgpt-mermaid-\_r_sf\_ .node ellipse,#chatgpt-mermaid-\_r_sf\_ .node polygon,#chatgpt-mermaid-\_r_sf\_ .node path{fill:rgb(229, 243, 255);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_sf\_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-\_r_sf\_ .mermaid-decision .label-container{fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-dasharray:2,2;}#chatgpt-mermaid-\_r_sf\_ .edgePaths .flowchart-link{stroke:rgb(143, 143, 143);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-\_r_sf\_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_sf\_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}StartEnter number of apartmentsEnter apartment detailsCalculate units consumedCalculate progressive tariffAdd fixed chargesUnits below 100?Apply 10% rebateNo rebateCalculate final billCompare recorded andcalculated billIdentify discrepanciesMore apartments?Rank by consumptionDisplay bills and rankingStopYesNoYesNo

## 4. Python Source Code

```
# Smart Electricity Billing for Multiple Apartmentsn = int(input("Enter number of apartments: "))apartments = []for i in range(n):    print("\nApartment", i + 1)    apt_no = input("Enter apartment number: ")    previous = int(input("Enter previous meter reading: "))    current = int(input("Enter current meter reading: "))    recorded_bill = float(input("Enter recorded bill amount: "))    # Validate meter readings    if current < previous:        print("Invalid meter readings!")        continue    units = current - previous    # Progressive tariff calculation    if units <= 100:        energy_charge = units * 2    elif units <= 200:        energy_charge = (100 * 2) + (units - 100) * 3    else:        energy_charge = (100 * 2) + (100 * 3) + (units - 200) * 5    # Fixed charge    fixed_charge = 50    subtotal = energy_charge + fixed_charge
```

## 5. Sample Input

```
Enter number of apartments: 3

Apartment 1
Enter apartment number: A101
Enter previous meter reading: 1000
Enter current meter reading: 1080
Enter recorded bill amount: 194

Apartment 2
Enter apartment number: A102
Enter previous meter reading: 2000
Enter current meter reading: 2150
Enter recorded bill amount: 500

Apartment 3
Enter apartment number: A103
Enter previous meter reading: 3000
Enter current meter reading: 3250
Enter recorded bill amount: 1000
```

## 6. Sample Output

```
------ ELECTRICITY BILL DETAILS ------

Apartment: A101
Units Consumed: 80
Energy Charge: Rs. 160
Fixed Charge: Rs. 50
Rebate: Rs. 21
Final Bill: Rs. 189
Recorded Bill: Rs. 194
Status: Discrepancy Found

Apartment: A102
Units Consumed: 150
Energy Charge: Rs. 350
Fixed Charge: Rs. 50
Rebate: Rs. 0
Final Bill: Rs. 400
Recorded Bill: Rs. 500
Status: Discrepancy Found

Apartment: A103
Units Consumed: 250
Energy Charge: Rs. 750
Fixed Charge: Rs. 50
Rebate: Rs. 0
Final Bill: Rs. 800
Recorded Bill: Rs. 1000
Status: Discrepancy Found

------ CONSUMPTION RANKING ------

1. A103 - 250 units
2. A102 - 150 units
3. A101 - 80 units

------ BILLING DISCREPANCIES ------

Apartment: A101 | Difference: Rs. 5
Apartment: A102 | Difference: Rs. 100
Apartment: A103 | Difference: Rs. 200

Total Apartments Processed: 3
```

## 7. Concepts Used in Python

1. Variables – Store apartment and billing details.
2. Conditional Statements – Apply progressive tariff rates.
3. Loops – Process multiple apartments.
4. Lists – Store apartment information.
5. Dictionaries – Maintain individual billing records.
6. Functions – Use built-in `sorted()` and `round()`.
7. Sorting – Rank apartments based on electricity consumption.

Conclusion: This program calculates electricity bills for multiple apartments, applies rebates and fixed charges, detects billing discrepancies, and ranks apartments based on their electricity consumption.
