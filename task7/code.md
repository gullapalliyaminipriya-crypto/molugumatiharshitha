# Library Borrowing and Fine Reconciliation – Python Program

## 1. Problem Statement

The Library Borrowing and Fine Reconciliation system analyses book borrowing and returning records using tuples. It stores book IDs, borrowing periods, and return delays. The program calculates fines for overdue books, identifies overdue records, checks book availability, and generates a final library report.

Rules:

- Each book has a unique Book ID.
- Borrowing period is 14 days.
- Fine is ₹5 per overdue day.
- Books returned within 14 days have no fine.
- A book is available after it is returned.
- A book not yet returned is considered unavailable.

## 2. Algorithm

1. Start the program.
2. Create a list of tuples containing Book ID, borrowing days, and return status.
3. Set the borrowing limit to 14 days.
4. Set the fine per overdue day to ₹5.
5. Read each book record.
6. Calculate overdue days by subtracting 14 from borrowing days.
7. If overdue days are greater than zero, calculate the fine.
8. Identify overdue books.
9. Check whether each book is available or unavailable.
10. Calculate the total fine.
11. Display the borrowing report.
12. Stop the program.

## 3. Flowchart

\#chatgpt-mermaid-\_r_if\_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(13, 13, 13);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-\_r_if\_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_if\_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_if\_ .error-icon{fill:rgb(243, 243, 243);}#chatgpt-mermaid-\_r_if\_ .error-text{fill:rgb(13, 13, 13);stroke:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_if\_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-\_r_if\_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-\_r_if\_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-\_r_if\_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-\_r_if\_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-\_r_if\_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-\_r_if\_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_if\_ .marker.cross{stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_if\_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-\_r_if\_ p{margin:0;}#chatgpt-mermaid-\_r_if\_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_if\_ .cluster-label text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_if\_ .cluster-label span{color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_if\_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-\_r_if\_ .label text,#chatgpt-mermaid-\_r_if\_ span{fill:rgb(13, 13, 13);color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_if\_ .node rect,#chatgpt-mermaid-\_r_if\_ .node circle,#chatgpt-mermaid-\_r_if\_ .node ellipse,#chatgpt-mermaid-\_r_if\_ .node polygon,#chatgpt-mermaid-\_r_if\_ .node path{fill:rgb(222, 234, 251);stroke:rgb(83, 154, 248);stroke-width:1px;}#chatgpt-mermaid-\_r_if\_ .rough-node .label text,#chatgpt-mermaid-\_r_if\_ .node .label text,#chatgpt-mermaid-\_r_if\_ .image-shape .label,#chatgpt-mermaid-\_r_if\_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-\_r_if\_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-\_r_if\_ .rough-node .label,#chatgpt-mermaid-\_r_if\_ .node .label,#chatgpt-mermaid-\_r_if\_ .image-shape .label,#chatgpt-mermaid-\_r_if\_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-\_r_if\_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-\_r_if\_ .root .anchor path{fill:rgb(143, 143, 143)!important;stroke-width:0;stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_if\_ .arrowheadPath{fill:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_if\_ .edgePath .path{stroke:rgb(143, 143, 143);stroke-width:1px;}#chatgpt-mermaid-\_r_if\_ .flowchart-link{stroke:rgb(143, 143, 143);fill:none;}#chatgpt-mermaid-\_r_if\_ .edgeLabel{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-\_r_if\_ .edgeLabel p{background-color:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_if\_ .edgeLabel rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_if\_ .labelBkg{background-color:rgba(252, 252, 252, 0.5);}#chatgpt-mermaid-\_r_if\_ .cluster rect{fill:rgb(243, 243, 243);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_if\_ .cluster text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_if\_ .cluster span{color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_if\_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(243, 243, 243);border:1px solid rgba(0, 0, 0, 0.1);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-\_r_if\_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_if\_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-\_r_if\_ .icon-shape,#chatgpt-mermaid-\_r_if\_ .image-shape{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-\_r_if\_ .icon-shape p,#chatgpt-mermaid-\_r_if\_ .image-shape p{background-color:rgb(252, 252, 252);padding:2px;}#chatgpt-mermaid-\_r_if\_ .icon-shape .label rect,#chatgpt-mermaid-\_r_if\_ .image-shape .label rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_if\_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-\_r_if\_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-\_r_if\_ .node .neo-node{stroke:rgb(83, 154, 248);}#chatgpt-mermaid-\_r_if\_ [data-look="neo"].node rect,#chatgpt-mermaid-\_r_if\_ [data-look="neo"].cluster rect,#chatgpt-mermaid-\_r_if\_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-\_r_if\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_if\_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-\_r_if\_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-\_r_if\_-gradient);stroke-width:1px;}#chatgpt-mermaid-\_r_if\_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_if\_ [data-look="neo"].node .neo-line path{stroke:rgb(83, 154, 248);filter:none;}#chatgpt-mermaid-\_r_if\_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-\_r_if\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_if\_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-\_r_if\_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-\_r_if\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_if\_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-\_r_if\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_if\_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(0, 79, 153);}#chatgpt-mermaid-\_r_if\_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(0, 79, 153);}#chatgpt-mermaid-\_r_if\_ .node tspan[font-weight="normal"],#chatgpt-mermaid-\_r_if\_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-\_r_if\_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-width:1px;}#chatgpt-mermaid-\_r_if\_ .node rect,#chatgpt-mermaid-\_r_if\_ .node circle,#chatgpt-mermaid-\_r_if\_ .node ellipse,#chatgpt-mermaid-\_r_if\_ .node polygon,#chatgpt-mermaid-\_r_if\_ .node path{fill:rgb(229, 243, 255);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_if\_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-\_r_if\_ .mermaid-decision .label-container{fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-dasharray:2,2;}#chatgpt-mermaid-\_r_if\_ .edgePaths .flowchart-link{stroke:rgb(143, 143, 143);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-\_r_if\_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_if\_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}StartCreate book recordsSet limit = 14 daysRead book tupleBook returned?Calculate overdue daysMark unavailableOverdue days 0?Calculate fineFine = 0Mark book availableUpdate total fineMore records?Display final reportStopYesNoYesNoYesNo

## 4. Python Source Code

```
# Library Borrowing and Fine Reconciliation# Tuple format:# (Book ID, Borrowing Days, Return Status)books = [    ("B101", 18, True),    ("B102", 10, True),    ("B103", 20, False),    ("B104", 14, True),    ("B105", 17, True)]BORROWING_LIMIT = 14FINE_PER_DAY = 5total_fine = 0overdue_count = 0available_count = 0unavailable_count = 0print("========== LIBRARY REPORT ==========")print("Book ID  Days  Overdue  Fine  Status")print("------------------------------------")for book in books:    book_id, days, returned = book    if returned:        overdue_days = max(0, days - BORROWING_LIMIT)        fine = overdue_days * FINE_PER_DAY        status = "Available"        available_count += 1
```

## 5. Sample Input

The following records are given in the program:

```
B101  18  True
B102  10  True
B103  20  False
B104  14  True
B105  17  True
```

## 6. Sample Output

```
========== LIBRARY REPORT ==========
Book ID  Days  Overdue  Fine  Status
------------------------------------
B101     18    4        20    Available
B102     10    0        0     Available
B103     20    6        0     Unavailable
B104     14    0        0     Available
B105     17    3        15    Available
------------------------------------
Total Overdue Books: 2
Available Books: 4
Unavailable Books: 1
Total Fine: Rs. 35
====================================
```

## 7. Result

The Library Borrowing and Fine Reconciliation program successfully analyses book records using tuples, calculates overdue fines, identifies overdue books, checks book availability, and displays the total fine amount.

Concepts used: Tuples, Lists, Loops, Conditional Statements, Arithmetic Operations, and Variables.
