inkling "2.0"

type GameState {
    position: number,
    velocity: number,
    angle: number,
    rotation: number
}

const left = -1
const right = 1

type Action {
    command: number<left, right>
}

type CartPoleConfig {
    unused: number
}

simulator the_simulator(action: Action, config: CartPoleConfig): GameState {
}

graph (input: GameState): Action {

    concept balance(input): Action {
        curriculum {
            source the_simulator
            lesson balancing {
                constraint {
                    unused: -1
                }
            }
        }
    }
    output balance
}
