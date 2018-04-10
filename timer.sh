rm -f *.dat *.png NFT
rm -r -f results
F0=0
FF=10
STEP=0.01
FILENAME="datos.dat"
python3 datos.py > datos.dat
python3 graficar.py "datos.dat"
#time -f "Tiempo compilando (C++): \t\t%e"  c++ NFT.cpp -o NFT
#time -f "Tiempo calculando (C++): \t\t%e" ./NFT $FILENAME $F0 $FF $STEP "transf_c.dat"
#time -f "Tiempo graficando (Python, C++): \t%e" python3 graficar.py "transf_c.dat"
#time -f "Tiempo calculando (Python): \t\t%e" python3 NFT.py $FILENAME $F0 $FF $STEP  "transf_python.dat"
#time -f "Tiempo graficando (Python, Python): \t%e" python3 graficar.py "transf_python.dat"
#time -f "Tiempo calculando (Julia): \t\t%e" julia NFT.jl $FILENAME $F0 $FF $STEP  "transf_julia.dat"
#time -f "Tiempo graficando (Python, Julia): \t%e" python3 graficar.py "transf_julia.dat"

# Cronometraje de todo:

echo "Ccomp"
COUNTER=0
MAX=10
while [  $COUNTER -lt $MAX ]; do
    time -f "%e"  c++ NFT.cpp -o NFT
    COUNTER=$((COUNTER+1))
done

echo "Crun"
COUNTER=0
while [  $COUNTER -lt $MAX ]; do
    time -f "%e" ./NFT $FILENAME $F0 $FF $STEP "transf_c.dat"
    COUNTER=$((COUNTER+1))
done

echo "python"
COUNTER=0
while [  $COUNTER -lt $MAX ]; do
    time -f "%e" python3 NFT.py $FILENAME $F0 $FF $STEP  "transf_python.dat"
    COUNTER=$((COUNTER+1))
done

echo "julia"
COUNTER=0
while [  $COUNTER -lt $MAX ]; do
    time -f "%e" julia NFT.jl $FILENAME $F0 $FF $STEP  "transf_julia.dat"
    COUNTER=$((COUNTER+1))
done


rm -f *.dat NFT
#mkdir results
#mv datos.png results/
#mv transf_c.png results/
#mv transf_python.png results/
#mv transf_julia.png results/
