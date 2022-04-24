# ButterWorthの周波数特性

```
> python plot_freq_characteristics.py -i data/butterworth.txt -o fig/ButterWorthLPFFreq.png -c config/ButterWorthLPFFreq.yaml
```

# Chevyshevの周波数特性

```
> python plot_freq_characteristics.py -i data/chebyshev.txt -o fig/ChebyshevLPFFreq.png -c config/ChebyshevLPFFreq.yaml 
```

# ButterWorthのstep応答

```
> python plot_step_responses.py -i data/step_input.txt -s data/butterworth_step_char.txt -o fig/butterworth_times_char.png -c config/ButterWorthLPFStep.yaml
```

# Chebyshevのstep応答

TODO: まだ試してない
