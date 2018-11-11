#!/bin/sh

CMDNAME=`basename $0`

for OPT in "$@"
do
  case $OPT in
    "-t" | "-finishtime" ) FLG_T="TRUE" ;;
    "-s" | "-saveoutput" ) FLG_S="TRUE" ;;
    "-e" | "-waitforenter" ) FLG_E="TRUE" ;;
      * ) echo "Usage: $CMDNAME [-t -finishtime] [-s -saveoutput] [-e -waitforenter]" 1>&2
          exit 1 ;;
  esac
done

START_SH_FILENAME=`readlink -f $0`
MAIN_PY_DIRNAME=`dirname $START_SH_FILENAME`
MAIN_PY_FILENAME="$MAIN_PY_DIRNAME/src/main.py"
LOG_FILE_NAME="$MAIN_PY_DIRNAME/log/mp2_shell_$(date +\%Y\%m\%d_\%H\%M\%S).log"

cd $MAIN_PY_DIRNAME
if [ "$FLG_S" = "TRUE" ]; then
mkdir -p $MAIN_PY_DIRNAME/log
  if [ "$FLG_T" = "TRUE" -a "$FLG_E" = "TRUE" ] ; then
    python3 -u $MAIN_PY_FILENAME -t True -e True | tee $LOG_FILE_NAME
  elif [ "$FLG_T" = "TRUE" ] ; then
    python3 -u $MAIN_PY_FILENAME -t True | tee $LOG_FILE_NAME
  elif [ "$FLG_E" = "TRUE" ] ; then
    python3 -u $MAIN_PY_FILENAME -e True | tee $LOG_FILE_NAME
  else
    python3 -u $MAIN_PY_FILENAME | tee $LOG_FILE_NAME
  fi
else
  if [ "$FLG_T" = "TRUE" -a "$FLG_E" = "TRUE" ] ; then
    python3 $MAIN_PY_FILENAME -t True -e True
  elif [ "$FLG_T" = "TRUE" ] ; then
    python3 $MAIN_PY_FILENAME -t True
  elif [ "$FLG_E" = "TRUE" ] ; then
    python3 $MAIN_PY_FILENAME -e True
  else
    python3 $MAIN_PY_FILENAME
  fi
fi
