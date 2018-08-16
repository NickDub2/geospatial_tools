
Vagrant.configure(2) do |config|
  vm_ram = ENV['VAGRANT_VM_RAM'] || 4096
  vm_cpu = ENV['VAGRANT_VM_CPU'] || 2
  config.vm.box = "ubuntu/trusty64"
  config.vm.network :forwarded_port, guest: 22, host: 5236
  config.vm.provision "shell", inline: "/bin/bash /vagrant/bootstrap.sh", privileged: false

end
