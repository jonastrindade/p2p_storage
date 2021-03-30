run_peer_1:
 	python3 peer.py ip1 port ../Key-values-files/key-values-files_peer1 ip2:port,ip3:port,ip4:port,ip5:port
run_peer_2:
 	python3 peer.py ip2 port ../Key-values-files/key-values-files_peer2 ip1:port,ip3:port,ip4:port,ip5:port
run_peer_3:
 	python3 peer.py ip3 port ../Key-values-files/key-values-files_peer3 ip1:port,ip2:port,ip4:port,ip5:port
run_peer_4:
 	python3 peer.py ip4 port ../Key-values-files/key-values-files_peer4 ip1:port,ip2:port,ip3:port,ip5:port
run_peer_5:
 	python3 peer.py ip5 port ../Key-values-files/key-values-files_peer5 ip1:port,ip2:port,ip3:port,ip4:port
run_client_1:
 	python3 client.py ip1 port 5,6,7
run_client_2:
 	python3 client.py ip2 port 1,2,3,4,5,9