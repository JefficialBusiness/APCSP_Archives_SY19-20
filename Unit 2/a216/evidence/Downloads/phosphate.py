print("phosphate works")

def monitor():
  try:
    ph_level = .3

    current = get_phosphate()
    mesg = "Phosphate level OK"
  
    if (current > ph_level):
      mesg = "Phosphate level too high!"
    elif (current < ph_level):
      mesg = "Phosphate level too low!"
  
  except:
    print("Unexpected error")

  return mesg

# Functiion to simulate actual fish tank monitoring
def get_phosphate():
  return .05