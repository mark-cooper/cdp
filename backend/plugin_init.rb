require 'csv'
require_relative 'monkey_array'

IDENTIFIERS = File.join(File.dirname(__FILE__), '..', 'identifiers.csv')
RESOURCES = File.join(File.dirname(__FILE__), '..', 'resources.csv')
puts "\n[CDP] Loading identifiers: #{IDENTIFIERS}\n\n"

ArchivesSpaceService.loaded_hook do
  ids = {}
  repos = {}
  results = []

  # gather ids and repo names
  CSV.foreach(IDENTIFIERS, headers: true) do |row|
    ids[row['unitid']] = row['repo_name']
    repos[row['repo_name']] = -1
  end
  puts "\n[CDP] Total identifiers: #{ids.count}\n\n"

  # get repo ids from name
  repos.keys.each do |repo_name|
    repos[repo_name] = Repository[name: repo_name].id
  end
  puts "\n[CDP] Repositories: #{repos.inspect}\n\n"

  # process ids
  ids.each do |id, repo_name|
    repo_id = repos.fetch(repo_name)

    RequestContext.open(repo_id: repo_id) do
      refs = IDLookup.new.find_by_ids(
        Resource,
        {
          repo_id: repo_id,
          identifier: "[\"#{id}\"]"
        }
      )
      raise "Id not found: #{id}" if refs.empty?
      puts "\n[CDP] #{refs} [#{refs.class}]\n\n"
      results << {
        'repo_id' => repo_id,
        'resource_id' => id,
        'resource_uri' => refs[0]['ref'],
      }
    end
  end
  puts "\n[CDP] Writing resources to CSV\n\n"
  results.to_csv(RESOURCES)
end
