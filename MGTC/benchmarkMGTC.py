from petbenchmarks.benchmarks import BenchmarkApproach

print('elements')
BenchmarkApproach(approach_name='MGTC-elements',
                  predictions_file_or_folder='MGTC_process_elements.json',
                  output_results='results-mgtc-elements',
                  relax_window=1)
BenchmarkApproach(approach_name='MGTC-elements-sharp',
                  predictions_file_or_folder='MGTC_process_elements.json',
                  output_results='results-mgtc-elements-sharp',
                  relax_window=0)
