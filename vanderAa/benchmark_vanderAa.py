from petbenchmarks.benchmarks import BenchmarkApproach

print('elements')
BenchmarkApproach(approach_name='vanderAa-elements',
                  predictions_file_or_folder='vanderAa_elements.json',
                  output_results='results-vanderAa-elements',
                  relax_window=1)
BenchmarkApproach(approach_name='vanderAa-elements-sharp',
                  predictions_file_or_folder='vanderAa_elements.json',
                  output_results='results-vanderAa-elements-sharp',
                  relax_window=0)

print('relations')
BenchmarkApproach(approach_name='vanderAa-relations',
                  predictions_file_or_folder='vanderAa_relations.json',
                  output_results='results-vanderAa-relations',
                  relax_window=1)
BenchmarkApproach(approach_name='vanderAa-relations-sharp',
                  predictions_file_or_folder='vanderAa_relations.json',
                  output_results='results-vanderAa-relations-sharp',
                  relax_window=0)
