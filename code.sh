#!/bin/bash

declare -a users

display_menu() {
  echo "1. voir tous les utilisateurs"
  echo "2. Creer un utilisateur"
  echo "3. Modifier utilisateur"
  echo "4. supprimer utilisateur"
  echo "5. verifier existance utilisateur"
  echo "6. historique"
  echo "7. Exit"
}


voir_utilisateurs() {
  if [ ${#users[@]} -eq 0 ]; then
    echo "aucun utilisateurs."
  else
    echo "All users:"
    for user in "${users[@]}"; do
      echo "$user"
    done
  fi
  echo "espace pour retourner au menu..."
  read -n 1 key
  if [[ $key == " " ]]; then
  return
  fi

}



creer_utilisateur() {
  read -p "saisir id utilisateur (obligatoire): " id
  read -p "saisir nom (obligatoire): " nom
  read -p "saisir age (obligatoire): " age
  read -p "saisir profession (obligatoire): " profession
  if [[ -z $id || -z $nom || -z $age || -z $profession ]]; then
    echo "Erreur: svp remplir tous les champs"
  else
    user_data="$id, $nom, $age, $profession "
    users+=("$user_data")
    echo "Utilisateur cree avec succes "
  fi
  echo "retourner au menu..."
  read -n 1 -s
}


modifier_utilisateur() {
  read -p "saisir id utilisateur a modifier (obligatoire): " id
  if [[ -z $id ]]; then
    echo "Erreur: svp saisir id utilisateur a modifier"
    return
  fi
  for i in "${!users[@]}"; do
    user="${users[$i]}"
    user_id=$(echo "$user" | awk -F', ' '{print $1}')
    if [ "$user_id" == "$id" ]; then
      read -p "saisir nouveau nom: " nom
      read -p "saisir nouveau age: " age
      read -p "saisir nouveau profession: " profession
      users[$i]="$id, $nom, $age, $profession"
      echo "utilisateur modifie avec succes "
      echo "retourner au menu..."
      read -n 1 -s
    fi
  done
}


verifier_existance() {
  read -p "saisir option de recherhce  (1 nom , 2 ID): " option
  case $option in
    1)
      read -p "saisir le nom pour chercher: " name
      for user in "${users[@]}"; do
        if echo "$user" | grep -q ", $name, "; then
          echo "$user"
          return 0
        fi
      done
      echo "utilisateur avec le nom de  $name n existe pas"
      return 1
      ;;
    2)
      read -p "saisir ID pour chercher : " id
      for user in "${users[@]}"; do
        if echo "$user" | grep -q "^$id, "; then
          echo "$user"
          return 0
        fi
      done
      echo "utilisateur avec le id  $id n existe pas"
      return 1
      ;;
    *)
      echo "option invalide . essayez de nouveau."
      return 1
      ;;
  esac
}



supprimer_utilisateur() {
  read -p "saisir ID utilisateur a supprimer (obligatoire): " id
  if [[ -z $id ]]; then
    echo "Erreur: svp saisir ID utilisateur a supprimer"
    return
  fi
  for i in "${!users[@]}"; do
    user="${users[$i]}"
    user_id=$(echo "$user" | awk -F', ' '{print $1}')
    if [ "$user_id" == "$id" ]; then
      unset users[$i]
      echo "utilisateur supprimee avec succes"
      echo "retourner au menu..."
      read -n 1 -s
    fi
  done
  echo "utilisateur avec le id  $id n existe pas"
}


voir_historique() {
  echo "Historique:"
  cat historique.txt
}



# Main loop
while true; do
  display_menu
  read -p "Entrer votre choix: " choice
  case $choice in
    1)
      voir_utilisateurs
      ;;
    2)
      creer_utilisateur
      ;;
    3)
      modifier_utilisateur
      ;;
    4)
      supprimer_utilisateur
      ;;
    5)
      verifier_existance
      ;;
         6)
      voir_historique
      ;;
    7)
      echo "a bientot "
      exit
      ;;
    *)
      echo "choix invalide . essayez de nouveau."
      ;;
  esac
  echo "$(date): option choisi par l utilisateur $choice" >> historique.txt
done