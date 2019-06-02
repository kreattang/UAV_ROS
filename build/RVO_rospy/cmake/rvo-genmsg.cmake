# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "rvo: 1 messages, 0 services")

set(MSG_I_FLAGS "-Irvo:/home/wenbing/Learning_ROS_ws/src/RVO_rospy/msg;-Igeometry_msgs:/opt/ros/kinetic/share/geometry_msgs/cmake/../msg;-Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(rvo_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/wenbing/Learning_ROS_ws/src/RVO_rospy/msg/Information.msg" NAME_WE)
add_custom_target(_rvo_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "rvo" "/home/wenbing/Learning_ROS_ws/src/RVO_rospy/msg/Information.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(rvo
  "/home/wenbing/Learning_ROS_ws/src/RVO_rospy/msg/Information.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/rvo
)

### Generating Services

### Generating Module File
_generate_module_cpp(rvo
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/rvo
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(rvo_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(rvo_generate_messages rvo_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/wenbing/Learning_ROS_ws/src/RVO_rospy/msg/Information.msg" NAME_WE)
add_dependencies(rvo_generate_messages_cpp _rvo_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(rvo_gencpp)
add_dependencies(rvo_gencpp rvo_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS rvo_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(rvo
  "/home/wenbing/Learning_ROS_ws/src/RVO_rospy/msg/Information.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/rvo
)

### Generating Services

### Generating Module File
_generate_module_eus(rvo
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/rvo
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(rvo_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(rvo_generate_messages rvo_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/wenbing/Learning_ROS_ws/src/RVO_rospy/msg/Information.msg" NAME_WE)
add_dependencies(rvo_generate_messages_eus _rvo_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(rvo_geneus)
add_dependencies(rvo_geneus rvo_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS rvo_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(rvo
  "/home/wenbing/Learning_ROS_ws/src/RVO_rospy/msg/Information.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/rvo
)

### Generating Services

### Generating Module File
_generate_module_lisp(rvo
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/rvo
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(rvo_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(rvo_generate_messages rvo_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/wenbing/Learning_ROS_ws/src/RVO_rospy/msg/Information.msg" NAME_WE)
add_dependencies(rvo_generate_messages_lisp _rvo_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(rvo_genlisp)
add_dependencies(rvo_genlisp rvo_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS rvo_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(rvo
  "/home/wenbing/Learning_ROS_ws/src/RVO_rospy/msg/Information.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/rvo
)

### Generating Services

### Generating Module File
_generate_module_nodejs(rvo
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/rvo
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(rvo_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(rvo_generate_messages rvo_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/wenbing/Learning_ROS_ws/src/RVO_rospy/msg/Information.msg" NAME_WE)
add_dependencies(rvo_generate_messages_nodejs _rvo_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(rvo_gennodejs)
add_dependencies(rvo_gennodejs rvo_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS rvo_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(rvo
  "/home/wenbing/Learning_ROS_ws/src/RVO_rospy/msg/Information.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/rvo
)

### Generating Services

### Generating Module File
_generate_module_py(rvo
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/rvo
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(rvo_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(rvo_generate_messages rvo_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/wenbing/Learning_ROS_ws/src/RVO_rospy/msg/Information.msg" NAME_WE)
add_dependencies(rvo_generate_messages_py _rvo_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(rvo_genpy)
add_dependencies(rvo_genpy rvo_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS rvo_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/rvo)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/rvo
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_cpp)
  add_dependencies(rvo_generate_messages_cpp geometry_msgs_generate_messages_cpp)
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(rvo_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/rvo)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/rvo
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_eus)
  add_dependencies(rvo_generate_messages_eus geometry_msgs_generate_messages_eus)
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(rvo_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/rvo)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/rvo
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_lisp)
  add_dependencies(rvo_generate_messages_lisp geometry_msgs_generate_messages_lisp)
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(rvo_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/rvo)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/rvo
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_nodejs)
  add_dependencies(rvo_generate_messages_nodejs geometry_msgs_generate_messages_nodejs)
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(rvo_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/rvo)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/rvo\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/rvo
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_py)
  add_dependencies(rvo_generate_messages_py geometry_msgs_generate_messages_py)
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(rvo_generate_messages_py std_msgs_generate_messages_py)
endif()
