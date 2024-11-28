#! \bin\bash

if [ $# -lt 3 ]; then													
    echo $0: "usage: $( basename $0 ) <input> <reference> <output>"
    exit 1;		    
fi 

Warp=$1
reference=$2
output=$3

wb_command -convert-warpfield -from-fnirt ${Warp}  ${reference} -to-itk ${output}