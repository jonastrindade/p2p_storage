#!/usr/bin/env python3

# ============================= Torrent - Peer =============================
# Sistema torrent para Redes de Computadores
# UFMG - 2020/2
# Desenvolvido por Jonas Ferreira da Trindade
# Março de 2021
# ============================================================================

import sys
import socket
import struct

def main():

  if len(sys.argv) != 5:
      print("favor passar ip, porto, key-value e peers vizinhos")
      return

  peer_address = sys.argv[1]
  peer_port = sys.argv[2]
  key_value_file = sys.argv[3]
  neighboring_peers = sys.argv[4]

  print(peer_address)
  print(peer_port)
  print(key_value_file)
  print(neighboring_peers)

if __name__ == "__main__":
    print(sys.version)
    main()

def carregar_chunks():
  # ler key_value_file
  # atribuir ao struct peer seus chunks
  # ler cada linha do chunk file
  # utilizar split para quebrar arquivo e 
  # atribuir id e value ao item do struct
  return true

def carregar_peers_vizinhos():
  # ler neighboring_peers
  # atribuir vizinhos ao peer
  # quebrar neighboring_peers por virgulas
  # atribuir ip e port dos peers vizinhos 
  # no struct
  return true

def flooding():
  # usar struct do peer
  # procurar nos neighboring_peers
  # chunks solicitados pelo client
  # QUERY 2
  # [ip: 4 bytes]
  # [porto: 2 bytes]
  # [peer-ttl: 2 bytes]
  # [n_chunks: 2 bytes]
  # [chunk_ids: n_chunks * 2 bytes]
  return true

def responder_client():
  # enviar chunks carregados
  # a partir da funcao carregar chunks
  # enviar response
  # CHUNKS_INFO 3
  # receber response
  # [n_chunks: 2 bytes]
  # [chunks_ids: n_chunks * 2 bytes]



