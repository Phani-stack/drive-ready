from abc import ABC, abstractmethod


class Prototype(ABC):

    @abstractmethod
    def clone(self):
        pass


class VMInstance(Prototype):

    def __init__(self, os, runtime, monitoring_agent, hostname, ip_address):
        self.os = os
        self.runtime = runtime
        self.monitoring_agent = monitoring_agent
        self.hostname = hostname
        self.ip_address = ip_address

    def clone(self):
        return VMInstance(self.os, self.runtime, self.monitoring_agent, self.hostname, self.ip_address)


class GpuVMInstance(VMInstance):
    def __init__(self, os, runtime, monitoring_agent, hostname, ip_address, gpu_type):
        super().__init__(os, runtime, monitoring_agent, hostname, ip_address)
        self.gpu_type = gpu_type

    def clone(self):
        return GpuVMInstance(self.os, self.runtime, self.monitoring_agent, self.hostname, self.ip_address, self.gpu_type)


class VMInstanceRegistry:

    def __init__(self):
        self.vm_instance_registry = {}

    def add_vm_instance(self, key, vm_instance):
        self.vm_instance_registry[key] = vm_instance

    def get_vm_instance(self, key):
        prototype = self.vm_instance_registry[key]

        return prototype.clone()

def fill_registry(registry):

    ubuntu_instance = VMInstance("Ubuntu 22.04", "Docker 1.2", "Datadog", None, None)
    registry.add_vm_instance("backend-server-v1", ubuntu_instance)

    gpu_instance = GpuVMInstance("Ubuntu 22.04", "Docker 1.2", "Datadog", "gpu-01", "123.41.23.12", "Nvidia")
    registry.add_vm_instance("gpu-instance-v2", gpu_instance)


registry = VMInstanceRegistry()

fill_registry(registry)

vm1 = registry.get_vm_instance("backend-server-v1")
vm2 = registry.get_vm_instance("backend-server-v1")

gpu1 = registry.get_vm_instance("gpu-instance-v2")
gpu2 = registry.get_vm_instance("gpu-instance-v2")

print(vm1 is vm2)
print(gpu1 is gpu2)

print(type(vm1).__name__)
print(type(gpu1).__name__)
