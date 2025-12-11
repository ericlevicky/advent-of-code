# Day 11: Reactor

You hear some loud beeping coming from a hatch in the floor of the factory, so you decide to check it out. Inside, you find several large electrical conduits and a ladder.

Climbing down the ladder, you discover the source of the beeping: a large, toroidal reactor which powers the factory above. Some Elves here are hurriedly running between the reactor and a nearby server rack, apparently trying to fix something.

One of the Elves notices you and rushes over. "It's a good thing you're here! We just installed a new server rack, but we aren't having any luck getting the reactor to communicate with it!" You glance around the room and see a tangle of cables and devices running from the server rack to the reactor. She rushes off, returning a moment later with a list of the devices and their outputs (your puzzle input).

For example:

```
aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
```

Each line gives the name of a device followed by a list of the devices to which its outputs are attached. So, `bbb: ddd eee` means that device `bbb` has two outputs, one leading to device `ddd` and the other leading to device `eee`.

The Elves are pretty sure that the issue isn't due to any specific device, but rather that the issue is triggered by data following some specific path through the devices. Data only ever flows from a device through its outputs; it can't flow backwards.

After dividing up the work, the Elves would like you to focus on the devices starting with the one next to you (an Elf hastily attaches a label which just says `you`) and ending with the main output to the reactor (which is the device with the label `out`).

To help the Elves figure out which path is causing the issue, they need you to find every path from `you` to `out`.

In this example, these are all of the paths from `you` to `out`:

1. `you → bbb → ddd → ggg → out`
2. `you → bbb → eee → out`
3. `you → ccc → ddd → ggg → out`
4. `you → ccc → eee → out`
5. `you → ccc → fff → out`

In total, there are 5 different paths leading from `you` to `out`.

**Puzzle question:** How many different paths lead from `you` to `out`?

## Part Two: Visiting dac and fft

Thanks in part to your analysis, the Elves have figured out a little bit about the issue. They now know that the problematic data path passes through both `dac` (a digital-to-analog converter) and `fft` (a device which performs a fast Fourier transform).

They're still not sure which specific path is the problem, and so they now need you to find every path from `svr` (the server rack) to `out`. However, the paths you find must all also visit both `dac` and `fft` (in any order).

For example:

```
svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
```

This new list of devices contains many paths from `svr` to `out`:

- `svr,aaa,fft,ccc,ddd,hub,fff,ggg,out`
- `svr,aaa,fft,ccc,ddd,hub,fff,hhh,out`
- `svr,aaa,fft,ccc,eee,dac,fff,ggg,out`
- `svr,aaa,fft,ccc,eee,dac,fff,hhh,out`
- `svr,bbb,tty,ccc,ddd,hub,fff,ggg,out`
- `svr,bbb,tty,ccc,ddd,hub,fff,hhh,out`
- `svr,bbb,tty,ccc,eee,dac,fff,ggg,out`
- `svr,bbb,tty,ccc,eee,dac,fff,hhh,out`

However, only 2 paths from `svr` to `out` visit both `dac` and `fft`.

**Puzzle question:** Find all the paths from `svr` to `out`. How many of those paths visit both `dac` and `fft`?

## Gotchas & Strategy

- **Exploding path counts:** Naively enumerating every path in a graph with branching fan-out blows up exponentially. We avoided materializing path lists and instead counted paths with memoized depth-first search (DFS) so each node is processed once per unique state.
- **Early termination:** We treat `out` as a sink; once the search reaches it we return immediately with either 1 or 0 depending on the visit requirements, which keeps recursion shallow and predictable.
- **Part 2 requirements:** Tracking whether both `dac` and `fft` were visited is tricky when the graph reuses nodes. We encoded those visits as bits in a small mask and threaded that mask through the DFS. The mask is part of the cache key, preventing double-counting while still letting us reuse sub-results.
- **Parsing quirks:** Device lines may contain extra whitespace. `parse_input` strips the key and splits the rest on whitespace so the adjacency list stays clean even with uneven formatting.
- **Order-agnostic constraints:** Because `dac` and `fft` can appear in any order, the bitmask solution is simpler than managing explicit sequences or path reconstructions.

## Explain Like I'm Five

Imagine a big playground with lots of slides and tunnels. You can only move forward from one tunnel to the next. First, we counted every possible way to crawl from the "you" tunnel to the "out" tunnel without retracing steps. Then the teachers asked us to only count the paths that also visit two special tunnels named "dac" and "fft" somewhere along the way. Instead of drawing every possible route (which would take forever), we used a clever trick: each time we enter a tunnel, we remember whether we've already seen the special ones. When we finally crawl out, we only shout "I found a path!" if both special tunnels were visited. This way we stay fast even when the playground is huge.
