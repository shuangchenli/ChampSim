binary=${1}
n_warm=${2}
n_sim=${3}
trace=${4}
results=${5}

(./bin/${binary} -warmup_instructions ${n_warm}000000 -simulation_instructions ${n_sim}000000 -traces ./trace/${trace}.trace.gz) &> ${results}/${trace}-${binary}.txt
