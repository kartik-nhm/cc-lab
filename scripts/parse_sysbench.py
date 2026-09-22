#!/usr/bin/env python3
"""
Sysbench Output Parser & Hypervisor Performance Comparator
Calculates percentage differences between Type-1 (Proxmox VE) and Type-2 (VMware Workstation) hypervisors.
"""


def compare_hypervisors():
    proxmox = {
        "hypervisor": "Proxmox VE (Type-1)",
        "eps": 1716.69,
        "total_time": 10.0004,
        "total_events": 17168,
        "min_lat": 0.57,
        "avg_lat": 0.58,
        "max_lat": 2.78,
        "p95_lat": 0.65,
    }

    vmware = {
        "hypervisor": "VMware Workstation (Type-2)",
        "eps": 1364.78,
        "total_time": 10.0007,
        "total_events": 13649,
        "min_lat": 0.67,
        "avg_lat": 0.73,
        "max_lat": 4.06,
        "p95_lat": 0.89,
    }

    eps_diff = ((proxmox["eps"] - vmware["eps"]) / vmware["eps"]) * 100
    events_diff = proxmox["total_events"] - vmware["total_events"]
    avg_lat_diff = ((vmware["avg_lat"] - proxmox["avg_lat"]) / vmware["avg_lat"]) * 100
    p95_lat_diff = ((vmware["p95_lat"] - proxmox["p95_lat"]) / vmware["p95_lat"]) * 100
    max_lat_diff = ((vmware["max_lat"] - proxmox["max_lat"]) / vmware["max_lat"]) * 100
    min_lat_diff = ((vmware["min_lat"] - proxmox["min_lat"]) / vmware["min_lat"]) * 100

    print("=========================================================================================")
    print("        HYPERVISOR CPU PERFORMANCE COMPARISON: TYPE-1 VS TYPE-2                          ")
    print("=========================================================================================")
    print(f"{'Metric':<30} {'Proxmox VE (Type-1)':<22} {'VMware (Type-2)':<20} {'Performance Delta'}")
    print("-----------------------------------------------------------------------------------------")
    print(f"{'Throughput (Events/sec)':<30} {proxmox['eps']:<22.2f} {vmware['eps']:<20.2f} +{eps_diff:.2f}% (Proxmox faster)")
    print(f"{'Total Events (10s)':<30} {proxmox['total_events']:<22} {vmware['total_events']:<20} +{events_diff:,} events (+{events_diff/vmware['total_events']*100:.2f}%)")
    print(f"{'Total Execution Time (s)':<30} {proxmox['total_time']:<22.4f} {vmware['total_time']:<20.4f} ~0.00% delta")
    print(f"{'Minimum Latency (ms)':<30} {proxmox['min_lat']:<22.2f} {vmware['min_lat']:<20.2f} Proxmox {vmware['min_lat']-proxmox['min_lat']:.2f}ms (-{min_lat_diff:.2f}%) lower")
    print(f"{'Average Latency (ms)':<30} {proxmox['avg_lat']:<22.2f} {vmware['avg_lat']:<20.2f} Proxmox {vmware['avg_lat']-proxmox['avg_lat']:.2f}ms (-{avg_lat_diff:.2f}%) lower")
    print(f"{'95th Percentile Latency (ms)':<30} {proxmox['p95_lat']:<22.2f} {vmware['p95_lat']:<20.2f} Proxmox {vmware['p95_lat']-proxmox['p95_lat']:.2f}ms (-{p95_lat_diff:.2f}%) lower")
    print(f"{'Maximum Latency (ms)':<30} {proxmox['max_lat']:<22.2f} {vmware['max_lat']:<20.2f} Proxmox {vmware['max_lat']-proxmox['max_lat']:.2f}ms (-{max_lat_diff:.2f}%) lower")
    print("=========================================================================================")


if __name__ == "__main__":
    compare_hypervisors()
