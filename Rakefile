require 'rubygems'
require 'rake'
require 'rdoc'
require 'date'
require 'yaml'
require 'tmpdir'
require 'shellwords'
require 'jekyll'

desc "Generate CV"
task :generate_CV do
  system "cd scripts && python ./generate_CV.py --abbreviate-authors && cd .."
  # system "cd scripts && python ./generate_CV.py && cd .."
  system "mv scripts/CV.pdf assets/pdf/"
end

desc "Generate static files"
task :generate do
  Jekyll::Site.new(Jekyll.configuration({
    "source"      => ".",
    "destination" => "_site"
    })).process
end


desc "Generate and deploy to Github"
task :deploy => [:generate] do
  Dir.mktmpdir do |tmp|
    system "mv _site/* #{tmp}"
    begin
      system "git checkout master"
    rescue Exception => e
      puts "Error: git command abort"
      exit -1
    end
    system "rm -rf *"
    system "mv #{tmp}/* ."

    system "git add --all"
    message = "updated at #{Time.now}"
    begin
      system "git commit -am #{message.shellescape}"
      system "git push origin master"
    rescue Exception => e
      puts "Error: git command abort"
      puts e
      exit -1
    end
    system "git checkout source-folio"
    puts "Deployed."
  end
end

task :default => :deploy
