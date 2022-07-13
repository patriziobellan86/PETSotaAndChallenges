from petbenchmarks.benchmarks import BenchmarkApproach

print('elements')
BenchmarkApproach(approach_name='Kruz-elements',
                  predictions_file_or_folder='Kruz_process_elements.json',
                  output_results='results-kruz-elements',
                  relax_window=1)
BenchmarkApproach(approach_name='Kruz-elements-sharp',
                  predictions_file_or_folder='Kruz_process_elements.json',
                  output_results='results-kruz-elements-sharp',
                  relax_window=0)

print('relations')
BenchmarkApproach(approach_name='Kruz-relations',
                  predictions_file_or_folder='Kruz_process_relations.json',
                  output_results='results-kruz-relations',
                  relax_window=1)
BenchmarkApproach(approach_name='Kruz-relations-sharp',
                  predictions_file_or_folder='Kruz_process_relations.json',
                  output_results='results-kruz-relations-sharp',
                  relax_window=0)
