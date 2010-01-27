## Uses

- the toaster oven in our lab

## Warning

I wouldn't breath in the fumes of the toasting process. Plenty of flux and glue and other chemicals in the PCB manufacturing process. Do this with the bay door open or outside.

## Background

Using this page as reference : <http://instruct1.cit.cornell.edu/courses/ee476/FinalProjects/s2006/ki38/Webpage/index.html> Specifically this reflow temperature curve characterization <http://instruct1.cit.cornell.edu/courses/ee476/FinalProjects/s2006/ki38/Webpage/kester.jpg>

Based on that the curve should look like

- room temp to 300Fahrenheit in ~90 seconds Preheating Zone
- 300F to 350F in ~90 seconds Soaking Zone
- 350F to 420F in 30 seconds peak Reflow Zone rise
- 420F back to 350F in 30 seconds Reflow Zone fall

I characterized the toaster we have in the lab with nothing in it

- starting@450
- 77F @ 0 seconds
- 120F@ 1:15
- 245F@ 3:30
- 300F@ 4:30
- 330F@ 5
- 357F@ 5:30
- 385F@ 6:00
- 400F?@ 6:30 (max of my thermometer)

## Process

Based on this I attempted

- 210 sec or so warmup
- 90 sec in \#1
- 90 sec in \#2
- 30
- 30 cooling from 400

What ended up happening was putting it in at around 250, figuring it would lose a lot of heat on opening the oven and then just watching until solder got shiny most everywhere I ended up chickening out before large polarized caps were able to finish because the oven reached 400+ degrees and I didn't want it to peak any higher than 420
