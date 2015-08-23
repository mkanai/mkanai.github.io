require 'rubygems'
require 'rake'
require 'rdoc'
require 'date'
require 'yaml'
require 'tmpdir'
require 'jekyll'

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
    system "git checkout master"
    system "rm -rf *"
    system "mv #{tmp}/* ."

    system "git add ."
    message = "updated at #{Time.now}"
    begin
      system "git commit -am #{message.shellescape}"
      system "git push origin master"
    rescue Exception => e
      puts "Error: git command abort"
      exit -1
    end
    system "git checkout source"
    puts "Deployed."
  end
end

task :default => :deploy

