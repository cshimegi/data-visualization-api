# -*- encoding: utf-8 -*-
# stub: vagrant-hostsupdater 1.2.1 ruby lib

Gem::Specification.new do |s|
  s.name = "vagrant-hostsupdater".freeze
  s.version = "1.2.1"

  s.required_rubygems_version = Gem::Requirement.new(">= 0".freeze) if s.respond_to? :required_rubygems_version=
  s.require_paths = ["lib".freeze]
  s.authors = ["Falk K\u00FChnel".freeze, "Chris Smith".freeze]
  s.date = "2020-12-03"
  s.description = "Enables Vagrant to update hosts file on the host machine".freeze
  s.email = ["fk@cogitatio.de".freeze, "chris@cgsmith.net".freeze]
  s.homepage = "https://github.com/cogitatio/vagrant-hostsupdater".freeze
  s.licenses = ["MIT".freeze]
  s.rubygems_version = "3.0.3".freeze
  s.summary = "Enables Vagrant to update hosts file on the host machine".freeze

  s.installed_by_version = "3.0.3" if s.respond_to? :installed_by_version

  if s.respond_to? :specification_version then
    s.specification_version = 4

    if Gem::Version.new(Gem::VERSION) >= Gem::Version.new('1.2.0') then
      s.add_development_dependency(%q<bundler>.freeze, ["~> 1.3"])
      s.add_development_dependency(%q<rake>.freeze, [">= 0"])
    else
      s.add_dependency(%q<bundler>.freeze, ["~> 1.3"])
      s.add_dependency(%q<rake>.freeze, [">= 0"])
    end
  else
    s.add_dependency(%q<bundler>.freeze, ["~> 1.3"])
    s.add_dependency(%q<rake>.freeze, [">= 0"])
  end
end
