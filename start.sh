#!/bin/bash

CMDNAME=`basename $0`

for OPT in "$@"
do
  case $OPT in
    "-t" | "--finishtime" ) FLG_T="TRUE" ;;
    "-s" | "--saveoutput" ) FLG_S="TRUE" ;;
    "-e" | "--waitforenter" ) FLG_E="TRUE" ;;
    "-nl" | "--no-loop" ) FLG_NL="TRUE" ;;
      * ) echo "Usage: $CMDNAME [-t --finishtime] [-s --saveoutput] [-e --waitforenter] [-nl --no-loop]" 1>&2
          exit 1 ;;
  esac
done

START_SH_FILENAME=`readlink -f $0`
MAIN_PY_DIRNAME=`dirname $START_SH_FILENAME`
MAIN_PY_FILENAME="$MAIN_PY_DIRNAME/src/main.py"
LOG_FILE_NAME="$MAIN_PY_DIRNAME/log/mp2_shell_$(date +\%Y\%m\%d_\%H\%M\%S).log"

cd $MAIN_PY_DIRNAME
mkdir -p $MAIN_PY_DIRNAME/log

if [ "$FLG_T" = "TRUE" ]; then
  OPTION_T="-t"
else
  OPTION_T=""
fi
if [ "$FLG_S" = "TRUE" ]; then
  OPTION_S_BEFORE="-u"
  OPTION_S_AFTER=" | tee $LOG_FILE_NAME"
else
  OPTION_S_BEFORE=""
  OPTION_S_AFTER=""
fi
if [ "$FLG_E" = "TRUE" ]; then
  OPTION_E="-e"
else
  OPTION_E=""
fi
if [ "$FLG_NL" = "TRUE" ]; then
  OPTION_L="-nl"
else
  OPTION_L=""
fi

# echo "python3 $OPTION_S_BEFORE $MAIN_PY_FILENAME $OPTION_T $OPTION_E $OPTION_L $OPTION_S_AFTER"
python3 $OPTION_S_BEFORE $MAIN_PY_FILENAME $OPTION_T $OPTION_E $OPTION_L $OPTION_S_AFTER
