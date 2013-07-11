#
# This script will essentially call the top_ips.sh script, but will
# "monitor" it and report on number of requests and how they change
# every 10 seconds.
#

if ARGV.length != 1
	puts "Usage: monitor_top_ips.sh [domain]"
	exit
end

domain = ARGV[0]

ips = {}

last_delta = {}

while true

	rates = {}
	top_ips = `bash top_ips.sh #{domain}`

	top_ips.each_line do |line|
		matches = /^\s*(\d+)\s*(.*)/.match(line)
		ip = matches[2]
		count = matches[1].to_i
		if ips.has_key?(ip)
			rate = (count - ips[ip])
			rates[ip] = rate
		end
		ips[ip] = count
	end

	rates.keys.each do |ip|
		if rates[ip] == 0
			last_delta.delete(ip) if last_delta.has_key?(ip)
			next
		end
		puts "#{ip}:\t\t#{rates[ip]} requests in last 10 seconds"
		puts "\tlast: #{last_delta[ip]}" if last_delta.has_key?(ip)
		last_delta[ip] = rates[ip]
	end
	puts "=" * 72
	sleep 10

end
