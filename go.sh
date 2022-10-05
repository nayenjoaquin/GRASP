FECHA=$(date +"%Y-%m-%d-%H-%M-%S")


for i in 001 .. 010 .. 001
do
    e1=$(python3 grasp.py -i 100-300-$i.txt -th 0.75 -d 0.9 -tL 90 -lsL 5 -tunning 1)

    e2=$(python3 grasp.py -i 100-300-$i.txt -th 0.80 -d 0.9 -tL 90 -lsL 5 -tunning 1)

    e3=$(python3 grasp.py -i 100-300-$i.txt -th 0.85 -d 0.85 -tL 90 -lsL 5 -tunning 1)

    linea="$i; $e1; $e2; $e3"
    echo $linea >> results/resultados-$FECHA.csv
done