using LinearAlgebra
using Plots

# Hadamard coin operator
function coin_operator(pos_state)
    C = [1/sqrt(2) 1/sqrt(2);
         1/sqrt(2) -1/sqrt(2)]
    return pos_state * C
end

# Other coin operator to make it interesting 
#function other_operator(pos_state)
    #C = [1/sqrt(2) 1/sqrt(2);
         #1/sqrt(2) -1/sqrt(2)]
    #return pos_state * C
#end

# Shift operator
function shift_operator(pos_state)
    new_pos_state = zeros(ComplexF64, size(pos_state))
    for i in 1:size(pos_state, 1)
        new_pos_state[i, 1] = pos_state[mod1(i - 1, size(pos_state, 1)), 1]
        new_pos_state[i, 2] = pos_state[mod1(i + 1, size(pos_state, 1)), 2]
    end
    return new_pos_state
end

function quantum_walk(steps, size=199)
    pos_state = zeros(ComplexF64, size, 2)
    #pos_state[(size + 1) ÷ 2, :] .= 1/sqrt(2)
    pos_state[(size + 1) ÷ 2, :] = [1/sqrt(2), -1/sqrt(2)] # start with the H|1> state: ~ |0> - |1>
    for _ in 1:steps
        pos_state = coin_operator(pos_state)
        pos_state = shift_operator(pos_state)
    end
    return pos_state
end

function plot_pdf(pos_state, steps, color)
    x_positions = -99:99
    prob_distribution = sum(abs.(pos_state).^2, dims=2)[:]
    plot!(x_positions, prob_distribution, xlabel=L"|x\rangle", ylabel="Probability", label="$(steps) steps", linecolor=color)
end

function main()
    walks = [(50, :blue), (100, :red), (150, :green), (200, :orange)]  # choose as many
    size = 199 # note this matches x_positions - should make it work better

    p = plot(grid=false)  # Initialize plot, get rid of grid
    for (steps, color) in walks
        pos_state = quantum_walk(steps, size)
        plot_pdf(pos_state, steps, color)
    end

    #title!("put something here")
    display(p)
end

main() 
