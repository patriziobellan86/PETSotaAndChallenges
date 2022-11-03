from petbenchmarks.benchmarks import BenchmarkApproach

print('elements')
BenchmarkApproach(approach_name='Qian-elements',
                  predictions_file_or_folder='Qian_elements.json',
                  output_results='results-Qian-elements',
                  relax_window=1)
BenchmarkApproach(approach_name='Qian-elements-sharp',
                  predictions_file_or_folder='Qian_elements.json',
                  output_results='results-Qian-elements-sharp',
                  relax_window=0)
