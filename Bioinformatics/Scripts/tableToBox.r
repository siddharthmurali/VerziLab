#This script is wrapped within cuffNormScript.sh

args<-commandArgs(TRUE)

library(reshape)
library(ggplot2)


data<-read.delim(args[1], header = TRUE);
#args[1] is argument 2 in cuffNormScript.sh

dataMelt <- melt(data, id = c("Genes"))

theme = theme_set(theme_minimal())
theme = theme_update( panel.grid.major.x=element_blank())
theme = theme_update(axis.line.y = element_blank(), axis.title.y=element_blank(), axis.text.y = element_text(colour="grey"), axis.ticks.y= element_line(colour="grey"))

ppc <- ggplot(data = dataMelt, aes(x = variable, y = value))

fileName<- paste("/Users/Sid/Documents/VerziLab/Bioinformatics/Plots/", args[2], ".png", sep='') 
# ^Change this path to preference. #args[2] is argument 3 in cuffNormScript.sh 

png(file = fileName)

ppc + geom_boxplot(aes(fill = variable)) + ylim(0,5) + stat_summary(fun.y=mean, colour="darkred", geom="point", shape=18, size=3,show_guide = FALSE)  + ggtitle(args[2]) + xlab("Sample") + ylab("FPKM")

dev.off()




