#only runs sample files, does not generate them
for i in {0..50}
do
  echo $i
  python3 solutions/sol.py < input/input$i.txt > output/output$i.txt
done
